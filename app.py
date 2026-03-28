import streamlit as st
import pickle
import pandas as pd
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")


movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
st.title("Movie Recommendation System")
import requests

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    
    response = requests.get(url)
    data = response.json()
    # st.write(data) 
    if data.get('poster_path'):
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    else:
        return "https://via.placeholder.com/500x750?text=No+Image"


def recommend_fun(movie):
    movie_index=movies[movies['title']==movie].index[0]
    dist=similarity[movie_index]
    movies_list=sorted(list(enumerate(dist)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    recommended_movies_poster=[]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movies.iloc[i[0]].movie_id))
    return recommended_movies,recommended_movies_poster




similarity=pickle.load(open('similarity.pkl','rb'))

selected_movie=st.selectbox("Write movie name",movies['title'].values)

if st.button("recommend"):
    names, posters=recommend_fun(selected_movie)
    
    col1, col2, col3 ,col4 , col5= st.columns(5)

    with col1:
        st.image(posters[0])
        st.text(names[0])

    with col2:
        st.image(posters[1])
        st.text(names[1])

    with col3:
        st.image(posters[2])
        st.text(names[2])

    with col4:
        st.image(posters[3])
        st.text(names[3])
    
    with col5:
        st.image(posters[4])
        st.text(names[4])


