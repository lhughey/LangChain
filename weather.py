# pip install -qU "langchain[anthropic]" to call the model
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather(city: str) -> str:
    """
    Get weather for a given city.
    
    Args:
        city (str): The name of the city to get weather for
        
    Returns:
        str: Weather information for the specified city
    """
    # TODO: Implement actual weather API integration
    return f"It's always sunny in {city}!"

def get_news(city: str) -> str:
    """
    Get news for a given city.
    
    Args:
        city (str): The name of the city to get news for
        
    Returns:
        str: News information for the specified city
    """
    # TODO: Implement actual news API integration
    return f"Latest news from {city}: Everything is great!"