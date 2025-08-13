from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import create_react_agent

from src.destanation_recommender.tools import why_this_destination
from src.destanation_recommender.prompts import (
    get_destination_based_on_user_preferences,
)

from src.utils.state import MainState
from src.utils.models import Destination, InformedDestination
from src.utils.utils import create_model


def destination_recommender(state: MainState) -> MainState:
    # Process user input and update the state graph
    model = create_model()
    llm = get_destination_based_on_user_preferences | model.with_structured_output(
        Destination
    )

    response = llm.invoke(
        {
            "language": state["user_preferences"].language,
            "location": state["user_preferences"].location,
            "travel_habits": state["user_preferences"].travel_habits,
            "interests": state["user_preferences"].interests,
            "personality": state["user_preferences"].personality,
            "budget": state["user_preferences"].budget,
            "travel_dates": state["user_preferences"].travel_dates,
        }
    )
    state["destination"] = response

    return state


def search_web_and_tell_why_this_location(state: MainState) -> MainState:
    locations = state["destination"].location
    questions = state["destination"].query_to_web
    needing_visa = state["destination"].need_visa
    user_preferences = state["user_preferences"]
    model = create_model()
    tools = [why_this_destination]
    model = model.bind_tools(tools)
    agent = create_react_agent(model, tools, response_format=InformedDestination)
    input_to_agent = {
        "messages": f"""
                                  You are an expert at giving reasons why these locations are great travel destinations.
                                  Please provide reasons for the following locations:
                                  {",".join(locations)}
                                  Visa requirements:
                                  {",".join([str(visa) for visa in needing_visa])}
                                  If you want to perform search please use this question:
                                  {"? ".join( questions)}.
                                  You also would need to create reasons for each location, please use answers from the web search, but you dont have too. And yes you can create from your database. If you dont have information about question, just tell some good reasons.
                                  
                                  """,
    }
    response = agent.invoke(input_to_agent)
    print(response["structured_response"])
    state["informed_destination"] = response["structured_response"]
    return state


destanation = StateGraph(MainState)
destanation.add_node("destination_recommender", destination_recommender)
destanation.add_node(
    "search_web_and_tell_why_this_location", search_web_and_tell_why_this_location
)
destanation.add_edge(START, "destination_recommender")
destanation.add_edge("destination_recommender", "search_web_and_tell_why_this_location")
destanation.add_edge("search_web_and_tell_why_this_location", END)

destanation = destanation.compile()
