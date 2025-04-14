import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

st.title("Dashboard")

df = pd.read_csv("imdb_top_1000.csv")
st.dataframe(df)

st.subheader("IMDB_Rating")
fig = px.histogram(df, x="IMDB_Rating", nbins=20, title="IMDB_Rating")
st.plotly_chart(fig)


df["Genre_Main"] = df["Genre"].apply(lambda x: x.split(",")[0].strip())

# Bar plot for IMDB Rating vs Series Title

top_movies = df.nlargest(10, "IMDB_Rating")
fig = px.bar(top_movies, x = "IMDB_Rating", y = "Series_Title",color= "IMDB_Rating",
             color_continuous_scale="viridis",
             title = "IMDB Rating vs Movie Name")
st.plotly_chart(fig)

st.markdown("This bar chart displays the **IMDb Ratings** for various **movie titles**, categorized by their **genre**.")

# Scatter plot for IMDB Rating vs No Of Votes

fig = px.scatter(df , x = "IMDB_Rating", y = "No_of_Votes", color = "IMDB_Rating",
                 title= "IMDB Rating vs No Of Votes")
st.plotly_chart(fig)

st.markdown("This scatter plot visualizes the relationship between **IMDb Ratings** and the **Number of Votes** a movie received.")

#Scatter plot for IMDB Rating vs Runtime

fig = px.scatter(df, x = "IMDB_Rating", y = "Runtime", color = "IMDB_Rating",
                 color_continuous_scale= "inferno",
                 title = "IMDB Rating vs Runtime")
st.plotly_chart(fig)

st.markdown("This scatter plot visualizes the relationship between **IMDb Ratings** and the **Runtime** of the movies.")

# Bar plot for No of Votes vs Series Title

top_movies = df.nlargest(10, "No_of_Votes")
fig = px.bar(top_movies, x = "No_of_Votes", y = "Series_Title", color = "No_of_Votes",
             color_continuous_scale="viridis", title= "Top 10 Movies by Number of Votes")
st.plotly_chart(fig)

st.markdown("This bar chart highlights the **top 10 movies** from the dataset with the **Highest No of Votes**.")

df['Runtime'] = df['Runtime'].str.extract('(\d+)').astype(float)

#Bar plot for Runtime vs Series Title

top_movies = df.nlargest(10 , "Runtime")
fig = px.bar(top_movies, x = "Runtime",y = "Series_Title", color = "Runtime",
             color_continuous_scale= "RdBu",
             title= "Top 10 Movies by Runtime")
st.plotly_chart(fig) 

st.markdown("This bar chart displays the **top 10 movies** from the dataset with the **Longest Runtime**.")

# Scatter plot for IMDB Rating vs Meta score
fig = px.scatter(df, x='IMDB_Rating', y='Meta_score', 
                 color='Meta_score',
                 color_continuous_scale="YLGnBu", 
                 title='IMDb Rating vs Meta Score')
st.plotly_chart(fig)

# Line plot for Released year vs IMDB Rating
top_movies = df.nlargest(10,"IMDB_Rating")
sns.lineplot(x='Released_Year', y='IMDB_Rating', data=top_movies, marker = "o", palette="Greens_r")
plt.title("IMDB Rating vs Released Year")
st.pyplot(plt)

st.markdown("This line plot visualizes the **IMDb ratings of the top 10 highest-rated movies**, along with their **release years**.")
#df['Gross'] = df['Gross'].str.extract('(\d+)').astype(float)
df['Gross'] = df['Gross'].str.replace(',', '').str.replace('$', '').astype(float)

# histogram plot for Gross Vs Director

top_movies = df.nlargest(10, "Gross")
fig = px.histogram(top_movies, x='Gross' , y = "Director", color='Director',
                   color_discrete_sequence=px.colors.qualitative.Plotly,
                   title='Gross vs Director')
st.plotly_chart(fig)

st.markdown("This bar chart highlights the **directors of the top 10 highest-grossing movies** in the dataset.")

# histogram plot for Genre vs No of votes
fig =px.histogram(df, x = "Genre_Main", y = "No_of_Votes",color= "Genre_Main",
            color_discrete_sequence=px.colors.qualitative.Plotly,
            title= "Genre vs No of Votes")
st.plotly_chart(fig)

st.markdown("This bar chart displays the **Number of Votes** for each **Genre** in the dataset.")

