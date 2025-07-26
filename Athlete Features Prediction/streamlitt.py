import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="🏋️ Fitness Jump Predictor", layout="centered")

# Load model
model = joblib.load('model.pkl')

# App Title
st.title("🏋️‍♂️ Fitness Jump Distance Predictor")
st.markdown("Enter your fitness metrics to predict your **Jump Distance (in cm)** ")

# Use columns for a cleaner layout
col1, col2 = st.columns(2)

with col1:
    age = st.number_input(" Age (in years)", min_value=5, max_value=100)
    weight = st.number_input(" Weight (kg)", min_value=10.0, max_value=200.0)
    bmi = st.number_input(" BMI", min_value=10.0, max_value=50.0)
    speed = st.number_input(" Sprinting Speed (m/s)", min_value=0.0, max_value=15.0)

with col2:
    height = st.number_input("Height (cm)", min_value=50.0, max_value=250.0)

    gender = st.selectbox("🧍 Gender", options=["Male", "Female"])
    gender_val = 0 if gender == "Male" else 1

    

# Predict button
if st.button(" Predict Jump Distance"):
    input_features = np.array([[age, gender_val, weight, height, bmi, speed]])
    prediction = model.predict(input_features)

    st.markdown("###  Predicted Jump Distance:")
    st.success(f"**{prediction[0]:.2f} cm** 🦘")

    st.balloons()

# Footer
st.markdown("---")
st.markdown("<center>Made with ❤️ using Streamlit</center>", unsafe_allow_html=True)
