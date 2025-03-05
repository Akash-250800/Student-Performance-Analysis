import streamlit as st
import pandas as pd
from joblib import load

# Load the trained model
model = load('student_performance_model_tuned.joblib')

# Streamlit app title and description
st.title("Student Performance Predictor")
st.write("Enter student details to predict their overall performance score (average of math, reading, and writing scores).")

# Input fields for features
st.subheader("Student Information")

gender = st.selectbox("Gender", options=["male", "female"])
race_ethnicity = st.selectbox("Race/Ethnicity", options=["group A", "group B", "group C", "group D", "group E"])
parental_education = st.selectbox(
    "Parental Level of Education",
    options=["some high school", "high school", "some college", "associate's degree", "bachelor's degree", "master's degree"]
)
lunch = st.selectbox("Lunch Type", options=["standard", "free/reduced"])
test_prep = st.selectbox("Test Preparation Course", options=["none", "completed"])

# Button to make prediction
if st.button("Predict Overall Score"):
    # Create a DataFrame with the input data
    input_data = pd.DataFrame({
        'gender': [gender],
        'race_ethnicity': [race_ethnicity],
        'parental_level_of_education': [parental_education],
        'lunch': [lunch],
        'test_preparation_course': [test_prep]
    })

    # Make prediction using the loaded model
    prediction = model.predict(input_data)[0]

    # Display the result
    st.success(f"Predicted Overall Score: {prediction:.2f}")
    st.write("Note: The overall score is an average of math, reading, and writing scores, ranging approximately from 0 to 100.")

# Footer
st.write("---")
st.write("Built with Streamlit and powered by a tuned RandomForest model.")