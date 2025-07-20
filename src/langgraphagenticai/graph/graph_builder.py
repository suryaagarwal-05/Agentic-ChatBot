from langgraph.graph import StateGraph, START, END
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.tool_bind_node import toolbot_node
from langgraph.prebuilt import ToolNode, tools_condition
from src.langgraphagenticai.tools.search_tool import get_tools


class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Langgraph compilation for basic chat bot.
        """

        self.basic_chatbot_node = BasicChatBotNode(self.llm)

        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process)
        
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)
        
    def build_search_graph(self):
        """
        graph bulader with tavily tool
        """
        
        tools = get_tools()
        tool_node = toolbot_node(tools)
        
        #Ggraph state declaration
        self.graph_builder = StateGraph(State)
        
        #node creation with tools
        self.graph_builder.add_node("chatbot", self.tool_node)
        self.graph_builder.add_node("search_chatbot", ToolNode(get_tools()))
        
        #Creating Edges
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot", tools_condition)
        self.graph_builder.add_edge("search_chatbot", END)
        
        
    def setup_graph(self, usecase:str):
        if usecase == "BASIC CHATBOT":
            self.basic_chatbot_build_graph()
            
        if usecase == "Toolbot":
            self.build_search_graph()

        return self.graph_builder.compile() 