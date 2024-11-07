import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("happy.csv")

happiness = df["happiness"]
gdp = df["gdp"]
generosity = df["generosity"]
corruption = df["corruption"]

options = ['Happiness', 'GDP','Generosity', 'Corruption']

st. header("In Search of Happiness")
xax = st.selectbox("Select the data for X-axis", options)
yax = st.selectbox("Select the data for Y-axis", options)
st.subheader(f"{xax} and {yax}")

def selection(xax, yax):
	d = {
		'Happiness':happiness,
		'GDP': gdp,
		'Generosity': generosity,
		'Corruption': corruption
	}

	return d[xax], d[yax]

xline, yline = selection(xax, yax)
figure = px.scatter(x= xline, y = yline, labels = {"x":xax , "y":yax})

st.plotly_chart(figure)


