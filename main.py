import streamlit as st

st.title("Weather Forecast For the Next 5 Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days:", min_value=1, max_value=5, help="Select the number of forecast days")
option = st.selectbox(" Select data to view", ("Temperature", "Sky"))
st.header(f"{option} conditions for the next {days} days at {place}")
