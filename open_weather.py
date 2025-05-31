# pip install --upgrade --quiet pyowm
import os
from dotenv import load_dotenv
from langchain_community.utilities import OpenWeatherMapAPIWrapper

load_dotenv()

def get_detailed_weather(city: str) -> str:
    """
    Get detailed weather information for a given city using OpenWeatherMap API.
    
    Args:
        city (str): The name of the city to get weather for
        
    Returns:
        str: Detailed weather information including temperature, conditions, and more
    """
    try:
        weather = OpenWeatherMapAPIWrapper()
        weather_data = weather.run(f"{city}")
        return weather_data
    except Exception as e:
        return f"Error getting detailed weather for {city}: {str(e)}"

#     weather_data = get_detailed_weather(f"{city}")
# print(weather_data)