import streamlit as st
import random
import altair as alt
import numpy as np
import pandas as pd

st.header('Midterm Data')

space_visits =pd.read_csv("Tableau Midterm Folders/near-earth-asteroids-discovered-over-time.csv")

st.write(space_visits)

st.sidebar.header("Pick two variables for your scatterplot")
x_val = st.sidebar.selectbox("Pick your x-axis",space_visits.select_dtypes(include=np.number).columns.tolist())
y_val = st.sidebar.selectbox("Pick your y-axis",space_visits.select_dtypes(include=np.number).columns.tolist())

bar = alt.Chart(space_visits).mark_bar().encode(
    x=x_val,
    y=y_val
)
st.altair_chart(bar, use_container_width=True)

