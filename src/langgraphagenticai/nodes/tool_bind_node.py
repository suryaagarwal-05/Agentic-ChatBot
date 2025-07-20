from src.langgraphagenticai.state.state import State

class ChatBotWithTools:
    def __init__(self,model):
        self.llm = model

    def toolbot_node(self, tools) -> dict:
        """Invoke llm with tool """
        
        llm_with_tool = self.llm.bind_tools(tools)
        
        def tool_node(state:State):
            return {"messages":self.llm_with_tool.invoke(state["messages"])}
        return tool_node