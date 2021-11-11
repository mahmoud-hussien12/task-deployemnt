from floralimited_recommender import flora_recommender
from rokomari_recommender import rokomari_recommendations
from bickroy_recommender import bickroy_recommendations

bickroy_recommendations
models = [
    {
        'name': 'Floralimited Recommender', 
        'handler': flora_recommender,
    },
    {
        'name': 'Rokomari Recommender', 
        'handler': rokomari_recommendations,
    },
    {
        'name': 'Bickroy Recommender', 
        'handler': bickroy_recommendations,
    }
]
style_placeholders = {
    '__primary_color__': 'black',
    '__secondary_color__': '#ddd'
}
