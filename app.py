import pickle
import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Function to fetch movie poster
def fetch_poster(movie_id, api_key):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    return f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else None

def recommend(movie, num_recommendations):
    try:
        index = movies[movies['title'] == movie].index[0]
    except IndexError:
        return ["No recommendations found"], []
    
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:num_recommendations + 1]:  # get top 'num_recommendations' recommendations
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id, api_key))

    # Ensure the lists have 'num_recommendations' elements
    while len(recommended_movie_names) < num_recommendations:
        recommended_movie_names.append("No more recommendations")
        recommended_movie_posters.append(None)
    
    return recommended_movie_names, recommended_movie_posters

# Your TMDB API key
api_key = "4532a3b09d94265338ff77714a69f5b4"

# Load data
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit UI
st.set_page_config(layout="wide", page_title="Movie Recommender System", page_icon="🎬")

# Header
st.title('Movie Recommender System')
st.write("Select a movie to get recommendations.")

# Dropdown for selecting movie
selected_movie = st.selectbox("Type or select a movie from the dropdown", movies['title'].values)

# Number of recommendations input
num_recommendations = st.number_input("Number of recommendations", min_value=1, max_value=10, value=5, step=1)

# Recommendation button
if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie, num_recommendations)
    
    # Display recommendations
    st.subheader(f"Top {num_recommendations} movies recommended for '{selected_movie}':")
    
    if "No recommendations found" in recommended_movie_names:
        st.warning("No recommendations found for the selected movie.")
    else:
        # Display recommended movies in a row layout
        cols = st.columns(num_recommendations)
        for col, movie_name, poster in zip(cols, recommended_movie_names, recommended_movie_posters):
            with col:
                st.write("")
                st.header(movie_name)
                if poster:
                    # Display poster with rounded corners
                    image = Image.open(BytesIO(requests.get(poster).content))
                    st.image(image, caption=movie_name, use_column_width=True, output_format='JPEG')
                else:
                    st.write("No poster available")

# Footer
st.markdown("---")
st.write("Developed by Prince")