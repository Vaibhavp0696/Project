import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

st.title("Dashboard")

df = pd.read_csv("imdb_top_1000.csv")
st.dataframe(df)