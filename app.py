import streamlit as st
import pickle
import pandas as pd
def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(enumerate(distances),key=lambda x: x[1],reverse=True)[1:6]
    recommend_list=[]
    for i in movies_list:
        print(recommend_list.append(movies.iloc[i[0]].title))
    return recommend_list
st.title("Movie Recommender System")
movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
# Google Drive file ID

similarity=pickle.load(open('similarity.pkl','rb'))
option=st.selectbox("Which movie you want to select?",movies['title'].values)
if st.button('Recommend'):
    rec=recommend(option)
    for i in rec:
        st.write(i)
