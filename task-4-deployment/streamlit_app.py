import streamlit as st
import pandas as pd
import numpy as np
import openpyxl
import pickle
from sklearn.metrics.pairwise import cosine_similarity

# creating menu, subheader
# add more options in the menu list to create a new window and do work
menu = ['Home', 'rokomari_bookstor_recommendar', 'extra']
choice = st.sidebar.selectbox("Menu", menu)

# necessary works for the rokomari_bookstor_recommender option
count_matrix=pickle.load(open('count_matrix.pkl','rb'))
cosine_sim = cosine_similarity(count_matrix, count_matrix)
indices = pd.read_csv('indices.csv')
df2 = pd.read_csv('df2.csv')
df2 = df2.set_index('Title')

def recommendations(title):
    recommended_books = []
    recommended_books_wa = []
    idx = indices[indices == title].index[0]
    print(idx)
    
    score_series = pd.Series(cosine_sim[idx]).sort_values(ascending=False)
    top_10_indexes = list(score_series.iloc[1:51].index)
    
    for i in top_10_indexes:
        recommended_books.append(list(df2.index)[i])
    for i in top_10_indexes:
        recommended_books_wa.append(list(df2.weighted_average)[i])
    Book_list_poplarity = pd.DataFrame(
        { 'Title':recommended_books,
          'Popularity': recommended_books_wa

        })
        
    return Book_list_poplarity.sort_values('Popularity',ascending=False)


# accessing different windows from the menu list. Add your option 
# with elif choice=='your option'
if choice == 'Home':
    st.subheader('Home')
elif choice == 'rokomari_bookstor_recommendar':
    st.subheader('rokomari_bookstor_recommendar')
    # st.success('it is a recommender')
    title = st.text_input('Enter book title')
    b = recommendations(title)
    st.write(b)
elif choice == 'extra':
    st.subheader('extra')
    # some tutorial ( will be deleted later)
    # Creating slider
    x = st.slider('x')
    st.write('square of', x, 'is', x*x)

    # Creating text input
    name = st.text_input('Enter a name')
    if len(name)!=0:
        st.write('The name is', name)

    # Creating checkbox
    if st.checkbox('Flash Sales'):
        st.write('ok')
    elif st.checkbox('Popular Chaldal'):
        st.write('ok')
    elif st.checkbox('Rokomari Books'):
        st.write('ok')
    
    # creating selectbox
    option = st.selectbox('which type of book you like the best', ['one', 'two', 'three'])
    st.write('good job')

    # creating multiselect
    options = st.multiselect('which types of book you like the best', ['one', 'two', 'three'])
    st.write('very good')
