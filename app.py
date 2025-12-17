import streamlit as st
import warnings
import json
from datetime import datetime
from dotenv import load_dotenv

# Import LangChain core components
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import create_agent

# Filter warnings
warnings.filterwarnings("ignore", category=UserWarning)

# 1. Page Configuration
st.set_page_config(page_title="AI Search Assistant", page_icon="🤖")
st.title("🤖 Assistant de Recherche IA")

# 2. Load Environment Variables
load_dotenv()

# 3. Initialize Agent
@st.cache_resource
def initialize_agent():
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    search_tool = TavilySearchResults(k=3)
    tools = [search_tool]
    
    # Get current date
    current_datetime = datetime.now().strftime("%d/%m/%Y à %H:%M")
    
    # SYSTEM PROMPT (In French as requested, but variable name in English)
    system_prompt = (
        f"Tu es un assistant IA utile et précis. Nous sommes le {current_datetime}. "
        "Tu as accès à un moteur de recherche pour trouver des informations récentes. "
        "Quand tu réponds, sois synthétique et clair."
    )
    
    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=system_prompt
    )
    return agent

agent = initialize_agent()

# 4. Session State Management
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        # If there are sources associated with this message, display them
        if "sources" in message:
            with st.expander("📚 Sources consultées"):
                for source in message["sources"]:
                    st.markdown(f"- [{source['title']}]({source['url']})")

# 5. User Input and Execution
if user_input := st.chat_input("Posez votre question..."):
    # Add user message to state
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate Response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("🕵️ *Recherche en cours...*")
        
        try:
            # Prepare history for the agent
            history_for_chain = []
            for msg in st.session_state.messages:
                if msg["role"] == "user":
                    history_for_chain.append(HumanMessage(content=msg["content"]))
                elif msg["role"] == "assistant":
                    history_for_chain.append(AIMessage(content=msg["content"]))
            
            # Run the Agent
            response = agent.invoke({"messages": history_for_chain})
            
            # Extract the final answer
            ai_content = response["messages"][-1].content
            
            # --- NEW: EXTRACT SOURCES ---
            sources = []
            # We iterate through all messages returned by the agent to find ToolMessages
            for msg in response["messages"]:
                if isinstance(msg, ToolMessage):
                    # Tavily results are usually JSON strings inside the 'content'
                    try:
                        results = json.loads(msg.content)
                        for res in results:
                            sources.append({"title": res.get("title", "Source"), "url": res.get("url", "#")})
                    except:
                        continue
            
            # Display Answer
            message_placeholder.markdown(ai_content)
            
            # Display Sources if any
            if sources:
                with st.expander("📚 Sources consultées"):
                    for source in sources:
                        st.markdown(f"- [{source['title']}]({source['url']})")
            
            # Save to history (including sources)
            st.session_state.messages.append({
                "role": "assistant", 
                "content": ai_content,
                "sources": sources # We save sources to keep them in history
            })
            
        except Exception as e:
            message_placeholder.error(f"Error: {e}")