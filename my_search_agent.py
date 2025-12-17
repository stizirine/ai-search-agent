import os
from dotenv import load_dotenv

# Import necessary classes
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage

# 1. Load environment variables
load_dotenv()

# 2. Setup Tools
# We put the tools in a list (we can add more later!)
search_tool = TavilySearch(max_results=3)
tools = [search_tool]

# 3. Setup the Brain (LLM)
# Crucial: We bind the tools to the LLM so it knows they exist
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# 4. Define the System Prompt (The Instructions)
# In LangChain 1.2.0+, we use system_prompt instead of a full prompt template
system_prompt = "You are a helpful AI assistant. You have access to a search engine. Use it when asked about current events or specific data."

# 5. Create the Agent
# In LangChain 1.2.0+, create_agent returns a compiled state graph
# that can be invoked directly
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=system_prompt
)

def run_agent():
    print("🤖 Agent is ready! Ask a question (or type 'quit' to exit).")
    
    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() in ['quit', 'exit']:
            print("Goodbye!")
            break
        
        print("Thinking...")
        
        try:
            # We run the agent with the user input
            # In LangChain 1.2.0+, the agent is invoked with messages
            response = agent.invoke({"messages": [HumanMessage(content=user_input)]})
            # The response contains messages, we need to get the last one
            last_message = response["messages"][-1]
            print(f"\n🤖 AI: {last_message.content}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    run_agent()