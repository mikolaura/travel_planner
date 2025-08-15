"""LangGraph single-node graph template.

Returns a predefined response. Replace logic and configuration as needed.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, TypedDict

from langchain_core.runnables import RunnableConfig
from langgraph.graph import StateGraph

from src.utils.utils import good_score
from src.utils.state import MainState, InputState
from src.agent_user.agent_user import agent_user
from src.destanation_recommender.destanation import destanation
from src.scorer.scorer import scorer
from src.weather.weather import weather

# Define the graph
graph = (
    StateGraph(MainState, input_schema=InputState)
    .add_node("agent_user", agent_user)
    .add_node("destination_recommender", destanation)
    .add_node("scorer", scorer)
    .add_node("weather", weather)
    .add_edge("__start__", "agent_user")
    .add_edge("agent_user", "destination_recommender")
    .add_edge("destination_recommender", "scorer")
    .add_conditional_edges(
        "scorer",
        good_score,
        {
            "continue": "weather",
            "return": "destination_recommender",
        },
    )
    .add_edge("scorer", "weather")
    .add_edge("weather", "__end__")
    .compile(name="New Graph")
)
