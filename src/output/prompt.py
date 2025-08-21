from langchain.prompts import ChatPromptTemplate

outline_prompt = ChatPromptTemplate.from_template(
    """
You are a travel assistant. I will provide you with information about one or more locations, including countries, cities, attractions, accommodations, transport options, and other relevant details. 

Your task is to generate a clear, structured OUTLINE that organizes the information logically for later expansion into a full travel guide.  

The outline should follow this structure:
Location 1:
    1. Overview of the location
    - General description
    - Key highlights
    - Cultural or historical importance

    2. Attractions and Points of Interest
    - Major landmarks
    - Hidden gems
    - Nature/outdoor spots

    3. Activities and Experiences
    - Recommended tours/activities
    - Seasonal events or festivals
    - Local experiences


    4. Food and Drink
    - Local cuisine highlights
    - Notable restaurants, cafés, or markets

    5. Practical Information
    - Best time to visit
    - Safety tips
    - Budget considerations

    6. Weather
    - Temperature
    - Feels like temperature
    - Conditions
    - Humidity
...
Location n:
    1. Overview of the location
    - General description
    - Key highlights
    - Cultural or historical importance

    2. Attractions and Points of Interest
    - Major landmarks
    - Hidden gems
    - Nature/outdoor spots

    3. Activities and Experiences
    - Recommended tours/activities
    - Seasonal events or festivals
    - Local experiences


    4. Food and Drink
    - Local cuisine highlights
    - Notable restaurants, cafés, or markets

    5. Practical Information
    - Best time to visit
    - Safety tips
    - Budget considerations

    6. Weather
    - Temperature
    - Feels like temperature
    - Conditions
    - Humidity

Make the outline hierarchical, well-organized, and ready for content expansion. Do not write full paragraphs, only structured bullet-point outlines.

This is all information:
{user_input}
    {user_preferences}
    {destination}
    {informed_destination}
    {location_scores}
    {weather}

"""
)

output_prompt = ChatPromptTemplate.from_template(
    """
You are a professional travel writer. I will provide you with an OUTLINE of locations and travel-related categories. 
Your task is to expand this outline into a well-written, detailed, and engaging travel guide. 

Guidelines for the output:
- Write in clear, natural, and reader-friendly language.
- Use full paragraphs, not bullet points.
- Expand each section with depth, detail, and examples.
- Highlight cultural insights, local stories, and practical advice.
- Balance informative content (history, logistics) with inspiration (atmosphere, experiences).
- Keep the structure aligned with the outline but make the text flow naturally.
- Write as if preparing a guide for curious travelers who want both useful tips and immersive descriptions.

Here is the outline:
{outline}

Now, expand it into a complete travel text with engaging detail.
"""
)
