import streamlit as st
import plotly.express as px
from backend import get_data

# Create site elements
st.title("Weather Forecast For the Next 5 Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days:", min_value=1, max_value=5, help="Select the number of forecast days")
option = st.selectbox(" Select data to view", ("Temperature", "Sky"))
st.header(f"{option} conditions for the next {days} days at {place}")

try:
    if place:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperature = [dict["main"]["temp"]/10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperature, labels={"x": "Dates", "y": "Temperatures (C)"})
            st.plotly_chart(figure)
        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_path = [images[condition] for condition in sky_conditions]
            st.image(image_path, width=115)
except KeyError:
    st.info("You have entered a non-existent city. Please enter the correct name")
