from langchain.prompts import ChatPromptTemplate


get_destination_based_on_user_preferences = ChatPromptTemplate.from_template(
    """You are an expert at searching the best places to travel based on user preferences. Also tell me does that location need visa if person got passport from current location, use information in 2021. And give me questions to ask using web
    prefered languages: {language}
    current location: {location}
    travel habits: {travel_habits}
    interests: {interests}
    personality: {personality}
    budget: {budget}
    travel dates: {travel_dates}

    
    """
)
