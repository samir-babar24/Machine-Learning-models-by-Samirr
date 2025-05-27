import streamlit as st
import joblib
import numpy as np

model = joblib.load("crop_model.pkl")

st.set_page_config(page_title="Crop Recommendation App", layout="centered")
st.title("🌱 Crop Recommendation System")
st.write("Enter the soil and climate details to get the best crop suggestion!")

N = st.number_input("Nitrogen (N)", 0.0)
P = st.number_input("Phosphorus (P)", 0.0)
K = st.number_input("Potassium (K)", 0.0)
temperature = st.number_input("Temperature (°C)", 0.0)
humidity = st.number_input("Humidity (%)", 0.0)
ph = st.number_input("Soil pH", 0.0)
rainfall = st.number_input("Rainfall (mm)", 0.0)

if st.button("Predict Crop"):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)

    st.success(f"🌾 Recommended Crop: **{prediction[0]}**")
