from typing import Optional, TypedDict, Any, List
from src.utils.models import (
    UserPreferences,
    Destination,
    InformedDestination,
    LocationScores,
    Weather
)


class InputState(TypedDict):
    user_input: str


class MainState(TypedDict):
    user_input: str
    user_preferences: Optional[UserPreferences]
    destination: Optional[Destination]
    informed_destination: Optional[InformedDestination]
    location_scores: Optional[LocationScores]
    weather: Optional[Weather]
