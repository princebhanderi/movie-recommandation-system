# movie-recommandation-system
A content-based movie recommendation system built using Python, Scikit-learn, Streamlit, and the TMDb API. This system recommends movies based on user preferences such as genres, cast, crew, and plot summaries.

# 🎬 Movie Recommendation System

A content-based movie recommendation system that suggests movies similar to the user's selected title. Built using Python, Streamlit for the interactive UI, and TMDB API for fetching movie posters and additional metadata.

## 🚀 Features

- ✅ Content-based filtering using cosine similarity
- 🎥 Movie metadata includes genres, cast, crew, and plot
- 🧠 Machine learning backend using `Scikit-learn`
- 🌐 Integrated with TMDB API for poster images and movie details
- ⚡ Fast and lightweight Streamlit app with real-time suggestions
- 📦 Compressed `.pkl` files for efficient storage and deployment

## 🛠️ Tech Stack

- Python 🐍
- Streamlit
- Scikit-learn
- Pandas / NumPy
- TMDB API
- Gzip for model compression

## 🧩 How it Works

1. Movie metadata is processed and transformed into feature vectors.
2. Cosine similarity is calculated between the selected movie and all others.
3. Top N similar movies are fetched and displayed with posters using TMDB API.

## 🏁 Getting Started

To get this project up and running on your local machine:

```bash
# Clone the repository
git clone https://github.com/princebhanderi/movie-recommandation-system.git
cd movie-recommandation-system

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
