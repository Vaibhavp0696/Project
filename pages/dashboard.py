import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

st.title("Dashboard")

df = pd.read_csv("imdb_top_1000.csv")
st.dataframe(df)

st.subheader("IMDB_Rating")
fig = px.histogram(df, x="IMDB_Rating", nbins=20, title="IMDB_Rating")
st.plotly_chart(fig)

df["Genre_Main"] = df["Genre"].apply(lambda x: x.split(",")[0].strip())
fig = px.bar(df, x = "Genre_Main", y = "Series_Title",color= "Genre_Main",
             title = "IMDB Rating vs Series Title")
st.plotly_chart(fig)

st.markdown("This bar chart displays the **IMDb Ratings** for various **movie titles**, categorized by their **genre**.")

fig = px.scatter(df , x = "IMDB_Rating", y = "No_of_Votes", color = "IMDB_Rating",
                 title= "IMDB Rating vs No Of Votes")
st.plotly_chart(fig)

st.markdown("This scatter plot visualizes the relationship between **IMDb Ratings** and the **Number of Votes** a movie received.")

