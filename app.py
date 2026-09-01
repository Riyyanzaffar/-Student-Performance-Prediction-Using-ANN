import streamlit as st
import pandas as pd

# 1. App ka Title (Website ka Header)
st.title("🎓 Student Performance Prediction App")
st.write("Apni details enter karein aur apna predicted final grade dekhein.")

# 2. User Input Section (Jo aapne Colab ke end mein banaya tha)
st.sidebar.header("User Inputs")
study_hours = st.sidebar.slider("Study Hours Per Week", 0, 40, 15)
attendance = st.sidebar.slider("Attendance Rate (%)", 50, 100, 85)

# 3. Prediction Button aur Result
if st.sidebar.button("Predict Grade"):
    # Yeh aap ka Colab wala prediction formula / logic hai
    predicted_grade = 50 + (study_hours * 0.8) + (attendance * 0.3)
    st.success(f"Aap ka Predicted Final Grade hai: **{round(predicted_grade, 2)}**")

# 4. Model Results Table
st.header("Model Comparison")
results_data = {
    'Model': ['Model 1', 'Model 2', 'Model 3'],
    'Activation': ['ReLU', 'Tanh', 'Sigmoid'],
    'Optimizer': ['Adam', 'SGD', 'RMSprop'],
    'Epochs': [50, 50, 100]
}
st.table(pd.DataFrame(results_data))
