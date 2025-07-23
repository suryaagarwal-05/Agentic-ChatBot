from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode

def get_tools():
    """
    Funciton to get tools to the node
    """
    tavily = TavilySearchResults(max_results=2)
    tavily
    tools = [tavily]
    
    return tools

def create_tool_node(tools):
    """
    creates and returns a tool node for the graph
    """
    return ToolNode(tools=tools)