import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# 1. Load environment variables from .env file
load_dotenv()

# 2. Initialize the LLM (Large Language Model)
# We use 'gpt-4o-mini' because it's fast and cheap for testing.
# temperature=0 means the model will be very factual and precise.
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def test_agent():
    print("🤖 Initializing the Brain...")
    
    # Simple test query
    query = "Hello! Who are you in one sentence?"
    
    # Invoke the model
    response = llm.invoke(query)
    
    # Print the result
    print(f"🤖 AI Answer: {response.content}")

if __name__ == "__main__":
    test_agent()