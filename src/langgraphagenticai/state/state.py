from typing_extensions import TypedDict, List
from typing import Annotated
from langgraph.graph.message import add_messages

class State(TypedDict):
    """State class for passing in graph builder"""

    messages :Annotated[List,add_messages ]
