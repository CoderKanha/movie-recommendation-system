import streamlit as st
import pickle
import joblib

st.title("Movie Recommendation System")
with open("movies_recommend.pickle", "rb") as file:
    movies_data_df = pickle.load(file)

movies_list = movies_data_df["title"].values

similarities = joblib.load("similarities.joblib")


def recommend_movies(movie_name):
    # Returns the top 5 movies similar to the given movie.

    recommend_list = []  # Stores recommended movie titles

    # Find the movie in the dataset
    movie_data = movies_data_df[movies_data_df["title"] == movie_name.lower()]

    if not movie_data.empty:
        movie_index = movie_data.index[0]  # Get the movie's index

        recommendations = similarities[movie_index]  # Get similarity scores

        # Sort movies by similarity score and exclude the input movie
        movie_list = sorted(
            enumerate(recommendations),
            reverse=True,
            key=lambda x: x[1]
        )[1:6]  # Select top 5 similar movies

        # Add recommended movie titles to the list
        for movie in movie_list:
            recommend_list.append(movies_data_df.iloc[movie[0]].title)

        return recommend_list  # Return recommended movies

    else:
        return []  # Return empty list if movie is not found



movie_name = st.selectbox("Movies", movies_list)

if st.button("Recommend"):
    st.write(f"Recommended movies for {movie_name} are:")
    m = recommend_movies(movie_name)
    for movie in m:
        st.write(movie)

