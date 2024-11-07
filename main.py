import streamlit as st


st.write('Weather forecast for the next days')
place = st.text_input("Place:", key="place")
forecast_days = st.slider("Forecast days", min_value=1, max_value = 5, key = "forecast_days")
# st.elect_slider("Forecast days", min_value=1, max_value = 5, key = "forecast_days")
# st.select_slider()
st.text_input("Select data to view", key="data")

st.write(f"Weather forecast for the next {place} days in {forecast_days}")