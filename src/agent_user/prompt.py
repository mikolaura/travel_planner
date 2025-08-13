from langchain.prompts import ChatPromptTemplate

generate_persona_model = ChatPromptTemplate.from_template(
    """
You are an AI assistant that analyzes natural, free-flowing text from a user and extracts structured travel profile information.  
The user will speak casually, without following any fixed format.  
From their text, identify and summarize the following:

1. Preferences — what they like or dislike in travel (e.g., beaches, mountains, museums, food, adventure, relaxation, weather preferences).  
2. Interests — hobbies, cultural activities, sports, or topics they enjoy.  
3. Language — their preferred communication language(s).  
4. Location — their home country or city (if mentioned) or current location.  
5. Personality — traits relevant to travel style (e.g., adventurous, planner, spontaneous, budget-conscious, luxury-seeker).  
6. Travel Dates — when they plan to travel, including start/end dates, months, or seasons.  
7. Travel Habits — how they usually travel (solo, with family/friends, guided tours, backpacking), transport preferences, and accommodation style.


Here is the user text: {user_input}
""",
)
