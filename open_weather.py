# pip install --upgrade --quiet pyowm
import os
from dotenv import load_dotenv

load_dotenv()

from langchain_community.utilities import OpenWeatherMapAPIWrapper

weather = OpenWeatherMapAPIWrapper()
weather_data = weather.run("London,GB")
print(weather_data)