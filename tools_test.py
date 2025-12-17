import os
from dotenv import load_dotenv
from langchain_tavily import TavilySearch

# 1. Load environment variables (TAVILY_API_KEY)
load_dotenv()

def test_search_tool():
    print("🔎 Testing the Search Tool...")

    # 2. Initialize the tool
    # max_results=3 means we want the top 3 results
    search_tool = TavilySearch(max_results=3)

    # 3. Define a query that requires real-time data
    query = "What is the current stock price of Apple (AAPL) today?"

    # 4. Run the search manually
    try:
        results = search_tool.invoke(query)
        
        # 5. Print results nicely
        for result in results:
            print(f"\n--- Result from: {result['url']} ---")
            # We limit the content display to keep it readable
            print(f"Content: {result['content'][:200]}...") 
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_search_tool()