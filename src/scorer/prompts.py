from langchain.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template(
    "You would need to create scores for each location, indicating their suitability for the user using reasons at person preferences:\n"
    "                                    language: {language}\n"
    "                                    location: {location}\n"
    "                                    travel_habits: {travel_habits}\n"
    "                                    interests: {interests}\n"
    "                                    personality: {personality}\n"
    "                                    budget: {budget}\n"
    "                                    travel_dates: {travel_dates}\n"
    "                                    Location list: {locations}"
)
