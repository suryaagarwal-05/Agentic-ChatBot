from langgraph.graph import StateGraph, START, END
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.tool_bind_node import  ChatBotWithTools
from langgraph.prebuilt import  tools_condition
from src.langgraphagenticai.tools.search_tool import get_tools, create_tool_node



class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    # def basic_chatbot_build_graph(self):
    #     """
    #     Langgraph compilation for basic chat bot.
    #     """

    #     self.basic_chatbot_node = BasicChatBotNode(self.llm)

    #     self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process)
        
    #     self.graph_builder.add_edge(START, "chatbot")
    #     self.graph_builder.add_edge("chatbot", END)
        
    def build_search_graph(self):
        """
        graph bulader with tavily tool
        """
        
        tools = get_tools()
        tool_node = create_tool_node(tools)
        print(tool_node)

        #Ggraph state declaration
        self.graph_builder = StateGraph(State)
        
        obj_chatbot = ChatBotWithTools(self.llm)
        chatbot_node = obj_chatbot.toolbot_node(tools)
        print(chatbot_node)
        
        #node creation with tools
        self.graph_builder.add_node("chatbot", chatbot_node)
        self.graph_builder.add_node("tools", tool_node)
        
        #Creating Edges
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot", tools_condition)
        self.graph_builder.add_edge("tools", "chatbot")
        
        
    def setup_graph(self, usecase:str):
        if usecase == "BASIC CHATBOT":
            self.basic_chatbot_build_graph()
            
        if usecase == "Toolbot":
            self.build_search_graph()

        return self.graph_builder.compile() 