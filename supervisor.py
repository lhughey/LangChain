from typing import Dict, List, Any
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain.tools import Tool
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class SupervisorAgent:
    def __init__(self):
        self.tools = self._register_tools()
        self.agent = self._create_agent()
        self.agent_executor = AgentExecutor(
            agent=self.agent,
            tools=self.tools,
            verbose=True
        )

    def _register_tools(self) -> List[Tool]:
        """Register all available tools."""
        from weather import get_weather
        from open_weather import get_detailed_weather
        
        return [
            Tool(
                name="get_weather",
                func=get_weather,
                description="Get the current weather for a given city"
            ),
            Tool(
                name="get_detailed_weather",
                func=get_detailed_weather,
                description="Get detailed weather information including temperature, conditions, and more for a given city"
            )
        ]

    def _create_agent(self):
        """Create the supervisor agent with appropriate prompt and model."""
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a supervisor agent that coordinates between different tools to accomplish user tasks.
            You should:
            1. Understand the user's request
            2. Determine which tools are needed
            3. Execute the tools in the correct order
            4. Combine and present the results in a meaningful way
            
            Always think step by step about what needs to be done."""),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ])

        llm = ChatOpenAI(
            model="gpt-4-turbo-preview",
            temperature=0
        )

        return create_openai_functions_agent(llm, self.tools, prompt)

    def process_request(self, user_input: str) -> Dict[str, Any]:
        """Process a user request using the supervisor agent."""
        return self.agent_executor.invoke({
            "input": user_input,
            "chat_history": []
        }) 