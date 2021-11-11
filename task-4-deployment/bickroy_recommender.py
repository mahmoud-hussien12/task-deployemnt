import pickle
import os
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

current_dir = os.path.dirname(__file__)
count_matrix=pickle.load(open(current_dir + '/bickroy.pkl','rb'))
cosine_sim = cosine_similarity(count_matrix, count_matrix)
dataset = pd.read_csv(current_dir + '/bickroy.csv')
dataset = dataset.set_index('title')
indices = pd.Series(dataset.index)

def bickroy_recommendations(title):
    recommended_gadgets = []
    matches = indices[indices == title]
    if matches.shape[0] == 0:
        f = indices.apply(lambda x: " ".join(x.split()))
        matches = f[f.str.contains(title)]
    if matches.shape[0] == 0:
        return []
    idx = matches.index[0]
    score_series = pd.Series(cosine_sim[idx]).sort_values(ascending=False)
    top_indexes = list(score_series.iloc[1:].index)
    items = list(dataset.index)
    
    for i in top_indexes:
        item = items[i]
        if item != title:
            recommended_gadgets.append(items[i])
        
    return list(set(recommended_gadgets))[:10]
