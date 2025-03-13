import pandas as pd
import numpy as np
from surprise import Dataset, Reader, SVD
from surprise import accuracy
from flask import Flask, request, jsonify

# Load MovieLens Dataset
movies = pd.read_csv('movies.csv')  # movieId, title, genres
ratings = pd.read_csv('ratings.csv')  # userId, movieId, rating, timestamp

# Drop timestamp column
ratings.drop(columns=['timestamp'], inplace=True)

# Ensure movieId is integer for correct mapping
movies['movieId'] = movies['movieId'].astype(int)
ratings['movieId'] = ratings['movieId'].astype(int)

# Prepare dataset for Surprise Library
reader = Reader(rating_scale=(0.5, 5.0))
data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)

# Train on the full dataset
trainset = data.build_full_trainset()
model = SVD(n_epochs=20, random_state=42)
model.fit(trainset)

# Create a test set manually
testset = trainset.build_testset()
predictions = model.test(testset)

# Evaluate model
rmse = accuracy.rmse(predictions)
print(f"Model RMSE: {rmse:.4f}")

# Function to recommend movies
def recommend_movies(user_id, model, movies, ratings, top_n=10):
    user_id = int(user_id)  # Ensure user_id is an integer

    if user_id not in ratings['userId'].astype(int).values:
        # Recommend top-rated movies if user is new
        top_movies = ratings.groupby('movieId')['rating'].mean().nlargest(top_n).index
        return movies[movies['movieId'].isin(top_movies)][['movieId', 'title']]

    all_movie_ids = movies['movieId'].unique()
    rated_movies = ratings[ratings['userId'] == user_id]['movieId'].values
    unrated_movies = np.setdiff1d(all_movie_ids, rated_movies)

    if len(unrated_movies) == 0:
        # Recommend top-rated movies instead of empty list
        top_movies = ratings.groupby('movieId')['rating'].mean().nlargest(top_n).index
        return movies[movies['movieId'].isin(top_movies)][['movieId', 'title']]

    sampled_movies = np.random.choice(unrated_movies, min(len(unrated_movies), 500), replace=False)
    predictions = [model.predict(user_id, movie_id) for movie_id in sampled_movies]
    predictions.sort(key=lambda x: x.est, reverse=True)

    top_movies = [pred.iid for pred in predictions[:top_n]]
    recommended_movies = movies[movies['movieId'].isin(top_movies)]

    return recommended_movies[['movieId', 'title']]

# Flask API
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Movie Recommendation API! Use /recommend?user_id=<user_id>&top_n=<number>"

@app.route('/recommend', methods=['GET'])
def recommend():
    try:
        user_id = int(request.args.get('user_id'))
        top_n = int(request.args.get('top_n', 10))
        recommendations = recommend_movies(user_id, model, movies, ratings, top_n)
        return jsonify({"recommendations": recommendations.to_dict(orient='records')})
    except Exception as e:
        return jsonify({"error": str(e)}), 400  # Return error message

if __name__ == '__main__':
    app.run(debug=True)