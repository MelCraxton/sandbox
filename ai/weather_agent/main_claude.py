# This is needed just because of the computer security
import os
os.environ['GRPC_DEFAULT_SSL_ROOTS_FILE_PATH'] = '/tmp/corp-ca-bundle.pem'
os.environ['SSL_CERT_FILE'] = '/tmp/corp-ca-bundle.pem'
os.environ['REQUESTS_CA_BUNDLE'] = '/tmp/corp-ca-bundle.pem'

# Libraries
import anthropic
from anthropic import beta_tool
from dotenv import load_dotenv
from pathlib import Path

# This is needed just because of the computer security
load_dotenv(Path(__file__).resolve().parent.parent.parent / '.env')

# Usually just need
# load_dotenv()


@beta_tool
def get_weather(city: str) -> str:
    """Get weather for a given city.

    Args:
        city: The city to get weather for.
    """
    return f"Weather in {city}: sunny as f*ck, 35C"


@beta_tool
def get_location() -> str:
    """Get the location of the user.
    Use this when the user asks about the weather without specifying a city.
    """
    return "Rome, Italy"


client = anthropic.Anthropic()

system_prompt = """
You are a helpful weather assistant.
YOUR WORKFLOW:
1. If the user asks for the weather without specifying a location
- first call get_location() to find their location
- then call get_weather(city) with that location
2. If the user provides a city, then just call get_weather(city)
"""

user_query = input("Enter your query: ")

runner = client.beta.messages.tool_runner(
    model="claude-opus-4-6",
    max_tokens=16000,
    system=system_prompt,
    tools=[get_weather, get_location],
    messages=[{"role": "user", "content": user_query}],
)

for message in runner:
    for block in message.content:
        if block.type == "text":
            print(block.text)
