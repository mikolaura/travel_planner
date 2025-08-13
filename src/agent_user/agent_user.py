from langgraph.graph import StateGraph, START, END
from src.agent_user.prompt import generate_persona_model
from src.utils.state import MainState, InputState
from src.utils.utils import create_model
from src.utils.models import UserPreferences


def persona_modeler(state: MainState) -> MainState:
    """Create persona model from user input"""
    llm = create_model()
    llm = generate_persona_model | llm.with_structured_output(UserPreferences)
    persona_model = llm.invoke({"user_input": state["user_input"]})
    print(persona_model)
    return {"user_input": state["user_input"], "user_preferences": persona_model}


agent_user = StateGraph(MainState, input_schema=InputState)

agent_user.add_node("persona_modeler", persona_modeler)
agent_user.add_edge(START, "persona_modeler")
agent_user.add_edge("persona_modeler", END)
agent_user = agent_user.compile()
