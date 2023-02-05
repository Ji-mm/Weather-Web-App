import streamlit as st
import plotly.express as px

st.title("Weather Forecast For the Next 5 Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days:", min_value=1, max_value=5, help="Select the number of forecast days")
option = st.selectbox(" Select data to view", ("Temperature", "Sky"))
st.header(f"{option} conditions for the next {days} days at {place}")


def get_data(days):
    date = ["2022-01-23", "2022-01-21", "2022-01-20"]
    temperatures = [1, 2, 3]
    temperatures = [days * i for i in temperatures]
    return date, temperatures


d, t = get_data(days)
figure = px.line(x=d, y=t, labels={"x": "Dates", "y": "Temperatures (C)"})
st.plotly_chart(figure)
