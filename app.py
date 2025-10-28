import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load trained model
model = pickle.load(open("linear_model.pkl", "rb"))

st.set_page_config(page_title="Netflix Type Prediction", page_icon="🎬", layout="centered")

st.title("🎬 Netflix Type Prediction App")
st.write("Predict whether a Netflix title is a **Movie** or a **TV Show** based on key features.")

# Input fields
st.header("📥 Enter Feature Values")

country = st.number_input("Country (encoded)", min_value=0, step=1)
date_added = st.number_input("Year Added to Netflix", min_value=2000, max_value=2025, step=1)
release_year = st.number_input("Release Year (scaled)", step=0.1)
listed_in = st.number_input("Listed In (encoded)", min_value=0, step=1)
duration_min = st.number_input("Duration (minutes)", min_value=0, step=1)
num_seasons = st.number_input("Number of Seasons (log-transformed)", min_value=0.0, step=0.1)
rating_encoded = st.number_input("Rating (encoded)", min_value=0, step=1)

# Prepare input
features = np.array([[country, date_added, release_year, listed_in, duration_min, num_seasons, rating_encoded]])
columns = ['country', 'date_added', 'release_year', 'listed_in', 'duration_min', 'num_seasons', 'rating_encoded']
input_df = pd.DataFrame(features, columns=columns)

# Predict button
if st.button("🔮 Predict"):
    try:
        prediction = model.predict(input_df)[0]
        result = "🎥 Movie" if prediction == 1 else "📺 TV Show"
        st.success(f"**Prediction:** {result}")
    except Exception as e:
        st.error(f"Error: {str(e)}")
