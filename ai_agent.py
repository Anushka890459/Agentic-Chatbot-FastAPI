import os
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY=os.getenv("GROQ_API_KEY")
TAVILY_API_KEY=os.getenv("TAVILY_API_KEY")


GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    # 1. LLM selection based on provider
    if provider == "Groq":
        llm = ChatGroq(model=llm_id)
    elif provider == "OpenAI":
        llm = ChatOpenAI(model=llm_id)
    else:
        return "Error: Invalid Provider"

    # 2. Tools setup
    tools = [TavilySearchResults(max_results=2)] if allow_search else []

    # 3. Create Agent (Inside function for dynamic updates)
    agent = create_react_agent(
        model=llm,
        tools=tools
    )

    # 4. Invoke logic
    try:
        response = agent.invoke(
            {
                "messages": [
                    SystemMessage(content=system_prompt),
                    HumanMessage(content=query)
                ]
            }
        )
        
        # Return only the content of the last AI message
        return {"response":response["messages"][-1].content}

    except Exception as e:
        return f"Error: {str(e)}"