import os
os.environ['GRPC_DEFAULT_SSL_ROOTS_FILE_PATH'] = '/tmp/corp-ca-bundle.pem'
os.environ['SSL_CERT_FILE'] = '/tmp/corp-ca-bundle.pem'
os.environ['REQUESTS_CA_BUNDLE'] = '/tmp/corp-ca-bundle.pem'

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.agents import create_agent

from pathlib import Path
load_dotenv(Path(__file__).resolve().parent.parent.parent / '.env')


def get_weather(city: str):
    """Get weather for a given city"""
    return {'condition': 'sunny as f*ck', 'temperature': 35}


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature = 0.7,
    transport="rest",
)


agent = create_agent(
    model=llm, 
    tools=[get_weather]
)

# response = llm.invoke('How is the weather in Rome today?')

response = agent.invoke(
    {'messages':[{'role': 'user', 
                  'content':'How is the weather in Rome?'}]})
print(response['messages'][-1].content)