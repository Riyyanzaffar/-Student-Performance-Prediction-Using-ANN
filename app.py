import streamlit as st

st.title("🎓 Student Performance Prediction Dashboard")
st.write("Welcome to the ANN Student Performance Model Dashboard!")

# Sidebar inputs
st.sidebar.header("User Inputs")
study_hours = st.sidebar.slider("Study Hours Per Week", 0, 40, 15)
attendance = st.sidebar.slider("Attendance Rate (%)", 50, 100, 85)

# Simple Prediction Output
if st.sidebar.button("Predict Final Grade"):
    predicted_grade = min(100, round(50 + (study_hours * 0.8) + (attendance * 0.3), 2))
    st.success(f"🎯 Predicted Final Grade: **{predicted_grade} / 100**")

st.info("App successfully deployed on Streamlit Cloud!")
