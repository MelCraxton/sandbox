# This is needed just becuase of the computer security
import os
os.environ['GRPC_DEFAULT_SSL_ROOTS_FILE_PATH'] = os.path.expanduser('~/.ssl/combined-ca-bundle.pem')
os.environ['SSL_CERT_FILE'] = os.path.expanduser('~/.ssl/combined-ca-bundle.pem')
os.environ['REQUESTS_CA_BUNDLE'] = os.path.expanduser('~/.ssl/combined-ca-bundle.pem')
from pathlib import Path

# Libraries 
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.postgres import PostgresSaver
from dotenv import load_dotenv
from langchain.agents import create_agent
import requests

load_dotenv(Path(__file__).parent / ".env")
DB_URI = os.getenv("SUPABASE_DB_URI")

def get_weather(city: str):
    """Get weather for a given city. 
    Return temperature_fahrenheit value in Fahrenheit label for location such as US, Liberia, Burma
    Return temperature in Celcius for locations that use this.
    """
    api_key = os.getenv("OPENWEATHER_API_KEY")
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params={
        "q": city,
        "appid": api_key,
        "units": 'metric'
    }
    
    response = requests.get(base_url, params=params)
    data=response.json()
    temperature_celicus = data['main']['temp']
    temperature_fahrenheit = temperature_celicus * 9/5 + 32
    return data, {'temperature_fahrenheit': temperature_fahrenheit}

def get_location():
    """Get the location of the user,
    use this when the user asks about the
    weather without specifying a city"""
    response = requests.get("https://ipapi.co/json", headers={'user-agent':'your-bot 0-1'})
    data = response.json()    
    city = data['city']
    country = data['country_name']
    return f"{city}, {country}"

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature = 0.7,
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
3. If the user does not provide a city, respond accrodingly and dont 
call the get_location() or get_weather() function
4. Use your knowledge to determine which temperature unit is standard for the 
given location
5.Present the weather information including temperature, condition, wind speed and 
any other details, but if the user does not provide a city then respond without calling
the functions.
"""

# This creates the db
with PostgresSaver.from_conn_string(DB_URI) as checkpointer:
    checkpointer.setup()

    agent = create_agent(
        model=llm, 
        tools=[get_weather, get_location],
        system_prompt = system_prompt,
        checkpointer=checkpointer
    )


    if __name__ == "__main__":

        while True:

            user_query = input("Enter the city for the weather: ")

            if user_query in ['bye', 'quit', 'exit']:
                print('See ya later, alligator!')
                break  
            
            response = agent.invoke({'messages':[{'role': 'user', 'content':user_query}]},
                                    {"configurable": {"thread_id":"1"}})
            # print(response['messages'][-1].content)

            for i in response['messages']:
                if i.type == 'human':
                    print('You: ', i.content)
                if i.type == 'ai':
                    print('Agent: ', i.content)

            # msg = next(m for m in reversed(response["messages"]) if m.content)

            # content = msg.content

            # if isinstance(content, list):
            #     print(content[0]["text"])
            # else:
            #     print(content)