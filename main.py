import weather
import os
from dotenv import load_dotenv



# This is a simple Python program that prints "Hello, World!" to the console.

#create a main method that will run the program

def main():
    print("Hello, World!")
    load_dotenv()
    #print(os.getenv("LANGCHAIN_API_KEY"))
    weather_result = weather.get_weather("San Francisco")
    print(f"Weather result: {weather_result}")
    print("Done")
    

if __name__ == "__main__":
    main()