import os
from dotenv import load_dotenv
from supervisor import SupervisorAgent



# This is a simple Python program that prints "Hello, World!" to the console.

#create a main method that will run the program

def main():
    # Load environment variables
    load_dotenv()
    
    # Initialize the supervisor agent
    supervisor = SupervisorAgent()
    
    # Example usage
    user_input = "What's the weather and latest news in San Francisco?"
    result = supervisor.process_request(user_input)
    
    print("\nSupervisor Agent Response:")
    print(result["output"])

if __name__ == "__main__":
    main()