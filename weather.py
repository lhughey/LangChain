# pip install -qU "langchain[anthropic]" to call the model
import os
from dotenv import load_dotenv
from langgraph.prebuilt import create_react_agent

load_dotenv()

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    print("calling get_weather")
    return f"It's always sunny in {city}!"

def get_news(city: str) -> str:
    """Get weather for a given city."""
    print("calling get_weather")
    return f"It's always sunny in {city}!"

agent = create_react_agent(
    model="openai:gpt-4.1",
   # model="anthropic:claude-opus-4-20250514",#"anthropic:claude-3-7-sonnet-latest",
    tools=[get_weather],
    prompt="You are a helpful assistant"
)

# Run the agent
response = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)
print(f"Agent response: {response}")