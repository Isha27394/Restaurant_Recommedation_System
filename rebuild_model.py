import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("Loading dataset from restaurant1.csv...")
df = pd.read_csv('restaurant1.csv')

print("Calculating cosine similarity matrix...")
count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(df['soup'])
cosine_sim = cosine_similarity(count_matrix, count_matrix)

indices = pd.Series(df.index, index=df['name']).drop_duplicates()

print("Exporting data and models...")
model_data = {
    'similarity_matrix': cosine_sim,
    'indices': indices,
    'restaurant_data': df[['name', 'cuisines', 'location', 'rate', 'approx_cost(for two people)']]
}

with open('restaurant.pkl', 'wb') as f:
    pickle.dump(model_data, f)
print("Process completed! Files saved as `restaurant.pkl`.")
