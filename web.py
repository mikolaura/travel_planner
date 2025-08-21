import streamlit as st
import os

st.set_page_config(page_title="👩‍🏫Academic helper")
st.title("✈Travel Planner")

google_api_key = st.sidebar.text_input("Google GenAI API Key")


def generate_response(user_input):
    os.environ["GOOGLE_API_KEY"] = google_api_key
    from src.travel_planner.graph import graph

    st.markdown(graph.invoke({"user_input": user_input})["output"].output)


with st.form("my_form"):
    user_input = st.text_area(
        "Tell about your preferences in travel, and what person are you(like where are you from, what do you like and so on)(you would need to wait up to 1 minute to get the response):",
    )
    submitted = st.form_submit_button("Submit")
    if not google_api_key:
        st.warning("Please enter your Google GenAI API key!", icon="⚠")
    if submitted and google_api_key:
        generate_response(user_input)
