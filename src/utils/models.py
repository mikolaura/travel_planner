from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any, TypedDict


class UserPreferences(BaseModel):
    language: List[str] = Field(..., description="Preferred languages of the user")
    location: str = Field(..., description="User's current location")
    travel_habits: List[str] = Field(..., description="User's travel habits")

    interests: List[str] = Field(..., description="List of user interests")
    personality: List[str] = Field(..., description="User's personality traits")

    budget: float = Field(..., description="User's budget for the trip in dollars USA")
    travel_dates: str = Field(
        ...,
        description="Preferred travel dates(in format 'YYYY-MM-DDtoYYYY-MM-DD')",
    )


class Destination(BaseModel):
    location: List[str] = Field(
        ..., description="List of recommended locations, in format(City, Country)"
    )
    need_visa: List[bool] = Field(
        ..., description="List indicating if a visa is needed for each location"
    )
    query_to_web: List[str] = Field(
        ...,
        description="Query to search the web for more information. Maximum 1 question per location",
    )


class Reasons(BaseModel):
    location: str = Field(..., description="Location in format (City, Country)")
    reasons: List[str] = Field(
        ...,
        description="List of reasons why this location is a great travel destination",
    )


class InformedDestination(BaseModel):
    need_visa: List[bool] = Field(
        ..., description="Indicates if a visa is needed for the location"
    )
    reasons: List[Reasons] = Field(
        ...,
        description="Reasons why this location is a great travel destination",
    )


class LocationScore(BaseModel):
    location: str = Field(..., description="Location in format (City, Country)")
    score: float = Field(
        ...,
        description="Score from 0 to 100 indicating the suitability of the location for the user",
    )


class LocationScores(BaseModel):

    scores: List[LocationScore] = Field(
        ...,
        description="List of scores from 0 to 100 indicating the suitability of the location",
    )

class Weather(BaseModel):
    temperature: List[float] = Field(
        ...,
        description="List of average temperature in given location for every day in celsium."
    )