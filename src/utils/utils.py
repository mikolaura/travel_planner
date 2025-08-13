from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain.chat_models import init_chat_model

from typing import Literal

from src.utils.state import MainState


def create_model():
    llm = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

    return llm


def good_score(state: MainState) -> Literal["continue", "return"]:
    """Logic to determine if the locations is good or not."""
    for score in state["location_scores"].scores:
        if score.score < 50:
            return "return"
    return "continue"
