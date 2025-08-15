from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import create_react_agent

from src.weather.tools import get_weather

from src.utils.models import Weather
from src.utils.utils import create_model
from src.utils.state import MainState

def get_weathers(state: MainState)-> MainState:
    dates = state['user_preferences'].travel_dates
    locations = state['destination'].location
    tools = [get_weather]
    model = create_model()
    model.bind_tools(tools)
    custom_prompt = """You are an AI agent that MUST always use the provided tools 
to answer any user query. Do NOT answer directly unless explicitly told 'no tools'.
Follow the ReAct pattern strictly.
"""
    agent = create_react_agent(model, tools,prompt=custom_prompt, response_format=Weather)
    agent_input = {
        "messages": f"""You are an expert for searching weather for given locations and dates using youre best tools.
            You need to tell weather for all given days and all given location.
    So here is locations: {",".join(locations)}
    And that is the dates: {dates}
    P.S. Don't forget that you can use tools
    """
    }
    response = agent.invoke(agent_input)
    print(response['structured_response'])
    state['weather'] = response['structured_response']
    return state

weather = StateGraph(MainState)
weather.add_node('get_weather', get_weathers)
weather.add_edge(START, "get_weather")
weather.add_edge("get_weather", END)
weather = weather.compile()
