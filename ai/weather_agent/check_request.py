import requests
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")

def get_weather(city: str):
    """Get weather for a given city"""
    api_key = os.getenv("OPENWEATHER_API_KEY")
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params={
        "q": city,
        "appid": api_key,
        "units": 'metric'
    }
    response = requests.get(base_url, params=params)
    data=response.json()
    return data


if __name__ == "__main__":
    city = input("Enter a city name: ")
    result = get_weather(city)
    print(result)
