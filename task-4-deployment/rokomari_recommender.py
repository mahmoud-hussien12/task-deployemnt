import pickle
import os
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

current_dir = os.path.dirname(__file__)
count_matrix=pickle.load(open(current_dir + '/count_matrix.pkl','rb'))
cosine_sim = cosine_similarity(count_matrix, count_matrix)
df2 = pd.read_csv(current_dir + '/df2.csv')
df2 = df2.set_index('Title')
indices = pd.Series(df2.index)

def rokomari_recommendations(title):
    recommended_books = []
    recommended_books_wa = []
    matches = indices[indices == title]
    if matches.shape[0] == 0:
        f = indices.apply(lambda x: " ".join(x.split()))
        matches = f[f.str.contains(title)]
    if matches.shape[0] == 0:
        return []
    idx = matches.index[0]
    print('index',idx)
    
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
