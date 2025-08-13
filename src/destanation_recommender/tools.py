from langchain.tools import tool
from ddgs import DDGS

from typing import List

from src.utils.models import UserPreferences


@tool
def why_this_destination(questions: List[str]) -> str:
    """
    This tool gives reasons why this location is a great travel destination
    Args:
        questions: List[str] - question to ask
    Returns:
        List[str] - reasons why this location is a great travel destination
    """
    print("TOOL IS USING")
    ddgs = DDGS()
    results = []
    for question in questions:
        response = ddgs.text(f"{question}", max_results=5)
        results.append(response)
    return results
