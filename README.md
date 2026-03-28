# 🎬 Movie Recommendation System

## About the Project

This is a simple movie recommendation system that suggests similar movies based on the one you select.
It uses a basic machine learning technique (cosine similarity) to find movies that are closely related.

I built this project to understand how recommendation systems work and to practice building a small web app using Streamlit.

---

## Features

* Select a movie from the dropdown
* Get top 5 similar movie recommendations
* View movie posters using TMDB API
* Simple and interactive UI

---

## Tech Used

* Python
* Pandas
* Streamlit
* Scikit-learn
* TMDB API

---

## How to Run

1. Clone the repository

```bash
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Add your API key
   Create a `.env` file and add:

```
TMDB_API_KEY=your_api_key_here
```

4. Run the app

```bash
streamlit run app.py
```

---

## Note

The `.pkl` files and dataset are not included in this repository because they are large.
You can generate them using the notebook or add them manually.

---

## Author

Ritesh Kandwal
