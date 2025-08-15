from langchain.tools import tool
import requests

@tool
def get_weather(location:str, date_start:str, date_end: str) -> list:
    """This tool gets all weather information for chosen location and dates
    Args:
        location:str in format: City
        date_start: str in format: YYYY-MM-DD
        date_end: str in format YYYY-MM-DD
    Return:
        list: weather information per day
    """
    print("WEATHER TOOL WAS USED!!!")
    r = requests.get(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{date_start}/{date_end}?unitGroup=metric&key=AMY4SZWQ4BPPTGAZYHZKNZALU&contentType=json")
    print(r.json())
    return r.json()['days']