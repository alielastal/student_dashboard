# app.py
import streamlit as st
from scripts.data_loader import load_data
from scripts.data_cleaning import clean_data
from scripts.predictor import load_model, predict

st.set_page_config(page_title="Student Performance Dashboard", layout="centered")

# Title
st.title("📊 Student Performance Dashboard")

# Load and clean data
df = load_data()
df = clean_data(df)

# Display data
st.subheader("Display raw data")
st.dataframe(df.head())

# Enter new data for forecasting
st.subheader("🔮 Predicting student results")
hours_studied = st.slider("Study hours", 0.0, 15.0, 5.0)
sleep_hours = st.slider("Sleep hours", 0.0, 12.0, 6.0)
attendance = st.slider("Attendance rate", 0.0, 100.0, 75.0)
previous_scores = st.slider("Previous grades", 0.0, 100.0, 70.0)

# Load the model and prediction
model = load_model()
if st.button("Calculate the prediction"):
    result = predict(model, [hours_studied, sleep_hours, attendance, previous_scores])
    st.success(f"🔔 Exam score prediction: {result:.2f}")