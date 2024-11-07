import streamlit as st
import plotly.express as px
from pygments.lexer import default

from backend import get_data

st.write('Weather forecast for the next days')

# Collecting inputs
place = st.text_input("Place:", key="place")
days = st.slider("Forecast days", min_value=1, max_value = 5, key = "days",
						  help = "Select the number of the forecated days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"), key="option")

# Function call
if place:
	filtered_data = get_data(place, days)

	st.subheader(f"{option} forecast for the next {place} days in {days}")


	if option == 'Temperature':
		temperatures = [dict["main"]["temp"] for dict in filtered_data]
		dates = [dict["dt_txt"] for dict in filtered_data]
		figure = px.line(x = dates, y = temperatures, labels={"x": "Date", "y": "Temperature (C)"})
		st.plotly_chart(figure)
	elif option == 'Sky':
		filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
		d={
			'Clear': 'images/clear.png',
			'Clouds': 'images/cloud.png',
			'Rain': 'images/rain.png',
			'Snow': 'images/snow.png',
		}
		data = [d[x] for x in filtered_data]
		st.image(data, width = 115 )

	#
# dates = ["01-11-2024", "02-11-2024", "03-11-2024"]
# temperatures = [10, 15, 17]
