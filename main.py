from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from tavily import TavilyClient
from langchain_tavily import TavilySearch


tavily= TavilyClient()


load_dotenv()

@tool
def search(query: str) -> str:
    """
    Tool that searches over internet using the tavily API.
    Args:
        query: The search query to search the internet for.
    Returns:
        The search result
    """
    print(f"Searching for: {query}")
    return tavily.search(query=query)

llm = ChatOpenAI(model='gpt-5')
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)

def main(): 
    print("Hello from langchain-course!")

    result = agent.invoke({"messages": HumanMessage(content="I want to 3 job openning for AI professional with langchain experience")})

    print(result)
if __name__ == "__main__":
    main()
