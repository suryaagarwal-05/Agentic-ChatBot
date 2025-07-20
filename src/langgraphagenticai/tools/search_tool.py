from langchain_tavily import TavilySearch

def get_tools():
    """
    Funciton to get tools to the node
    """
    tavily = TavilySearch(max_results=2)
    tools = [tavily]
    
    return tools