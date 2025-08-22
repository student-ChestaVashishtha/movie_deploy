import streamlit as st
import pickle
import pandas as pd
import requests
def fetch(title):
    api_key = "ff936319"
    url = f"http://www.omdbapi.com/?t={title}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()  # convert response to JSON
    return data['Poster']  # return the movie data
def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(enumerate(distances),key=lambda x: x[1],reverse=True)[1:6]
    recommend_list=[]
    poster_list=[]
    for i in movies_list:
        recommend_list.append(movies.iloc[i[0]].title)
        poster_list.append(fetch(movies.iloc[i[0]].title))
    return recommend_list,poster_list
st.title("Movie Recommender System")
movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
# Google Drive file ID

similarity=pickle.load(open('similarity.pkl','rb'))
option=st.selectbox("Which movie you want to select?",movies['title'].values)
if st.button('Recommend'):
    recommended_movie_names,recommended_movie_posters = recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
