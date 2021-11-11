import pickle
import os
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

current_dir = os.path.dirname(__file__)
tfidf_matrix=pickle.load(open(current_dir + '/floralimited.pkl','rb'))
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
df = pd.read_csv(current_dir + '/floralimited.csv')
df = df.set_index('name')
indices = pd.Series(df.index)

def flora_recommender(title):
    recommended_products = []
    matches = indices[indices == title]
    if matches.shape[0] == 0:
        f = indices.apply(lambda x: " ".join(x.split()))
        matches = f[f.str.contains(title)]
    if matches.shape[0] == 0:
        return []
    idx = matches.index[0]
    score_series = pd.Series(cosine_sim[idx]).sort_values(ascending=False)
    top_10_indexes = list(score_series.iloc[1:11].index)
    
    for i in top_10_indexes:
        recommended_products.append(list(df.index)[i])
    return recommended_products
