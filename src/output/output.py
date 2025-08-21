from langgraph.graph import StateGraph, START, END
from src.utils.state import MainState
from src.utils.utils import create_model
from src.utils.models import Outline, Output
from src.output.prompt import outline_prompt, output_prompt


def get_output(state: MainState) -> MainState:
    model_for_outline = create_model()
    llm = outline_prompt | model_for_outline.with_structured_output(Outline)
    output = llm.invoke(state)
    output_llm = output_prompt | create_model().with_structured_output(Output)
    output = output_llm.invoke({"outline": output})
    state["output"] = output
    return state


output = StateGraph(MainState)
output.add_node("get_output", get_output)
output.add_edge(START, "get_output")
output.add_edge("get_output", END)
output = output.compile()
