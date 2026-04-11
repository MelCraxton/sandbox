# This is needed just becuase of the computer security
import os
os.environ['GRPC_DEFAULT_SSL_ROOTS_FILE_PATH'] = os.path.expanduser('~/.ssl/combined-ca-bundle.pem')
os.environ['SSL_CERT_FILE'] = os.path.expanduser('~/.ssl/combined-ca-bundle.pem')
os.environ['REQUESTS_CA_BUNDLE'] = os.path.expanduser('~/.ssl/combined-ca-bundle.pem')

# Libraries 
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.agents import create_agent

# This is needed just becuase of the computer security
from pathlib import Path

# This is needed just becuase of the computer security
load_dotenv(Path(__file__).resolve().parent / '.env')

# Usually just need
# load_dotenv()


def get_weather(city: str):
    """Get weather for a given city"""
    return {'condition': 'sunny as f*ck', 'temperature': 35}

def get_location():
    """Get the location of the user,
    use this when the user asks about the
    weather without specifying a city"""
    return "Rome, Italy"

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature = 0.7,
    google_api_key=os.environ.get("GOOGLE_API_KEY"),
    # This is needed just becuase of the computer security
    transport="rest",
)

system_prompt = """
You are a helpful weather assistant.
YOUR WORKFLOW:
1.If the user asks for the weather without specifying a location
- first call get_location() to find their location
- then call get_weather(city) with that location 
2. If the user provides a city, then just call get_weather(city)
"""

agent = create_agent(
    model=llm, 
    tools=[get_weather, get_location],
    system_prompt = system_prompt
)

# response = llm.invoke('How is the weather in Rome today?')

user_query = input("Enter your query: ")

response = agent.invoke(
    {'messages':[{'role': 'user', 
                  'content':user_query}]})

print(response['messages'][-1].content)