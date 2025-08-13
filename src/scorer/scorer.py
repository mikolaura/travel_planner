from langgraph.graph import StateGraph, START, END

from src.utils.state import MainState
from src.utils.models import LocationScores
from src.utils.utils import create_model

from src.scorer.prompts import prompt


def score_location(state: MainState) -> MainState:
    locations = state["destination"].location
    model = create_model()
    llm = prompt | model.with_structured_output(LocationScores)
    result = llm.invoke(
        {
            "language": state["user_preferences"].language,
            "location": state["user_preferences"].location,
            "travel_habits": state["user_preferences"].travel_habits,
            "interests": state["user_preferences"].interests,
            "personality": state["user_preferences"].personality,
            "budget": state["user_preferences"].budget,
            "travel_dates": state["user_preferences"].travel_dates,
            "locations": locations,
        }
    )
    state["location_scores"] = result
    return state


scorer = StateGraph(MainState)
scorer.add_node("score_location", score_location)
scorer.add_edge(START, "score_location")
scorer.add_edge("score_location", END)
scorer = scorer.compile()
