import streamlit as st
import pickle
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Set page config
st.set_page_config(page_title="Stress Detection Predictor", layout="wide")

# Load the model
@st.cache_resource
def load_model():
    import os
    model_path = os.path.join(os.path.dirname(__file__), 'model_svc.pkl')
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model

model = load_model()

# Title and description
st.title("🧠 Stress Level Detection Predictor")
st.markdown("""
This application predicts stress detection using a Support Vector Classifier model trained on various health and lifestyle factors.
""")

# Create input columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("Health Metrics")
    age = st.slider("Age", 18, 80, 30)
    blood_pressure = st.slider("Blood Pressure (mmHg)", 80, 180, 120)
    cholesterol_level = st.slider("Cholesterol Level (mg/dL)", 100, 300, 200)
    blood_sugar_level = st.slider("Blood Sugar Level", 0, 10, 5)

with col2:
    st.subheader("Lifestyle Factors")
    work_hours = st.slider("Work Hours per Day", 1, 16, 8)
    sleep_duration = st.slider("Sleep Duration (hours)", 2, 12, 7)
    social_interactions = st.slider("Social Interactions", 0, 10, 5)
    smoking_habit = st.selectbox("Smoking Habit", [0, 1, 2])
    travel_time = st.slider("Travel Time (minutes)", 0, 120, 30)
    screen_time = st.slider("Screen Time (hours)", 0, 12, 4)
    physical_activity = st.slider("Physical Activity (hours)", 0, 5, 2)
    caffeine_intake = st.slider("Caffeine Intake (cups)", 0, 10, 2)
    alcohol_intake = st.slider("Alcohol Intake (units)", 0, 7, 2)
    sleep_quality = st.slider("Sleep Quality (1-10)", 1, 10, 7)

# Prepare input data
input_data = pd.DataFrame({
    'Age': [age],
    'Sleep_Duration': [sleep_duration],
    'Sleep_Quality': [sleep_quality],
    'Physical_Activity': [physical_activity],
    'Screen_Time': [screen_time],
    'Caffeine_Intake': [caffeine_intake],
    'Alcohol_Intake': [alcohol_intake],
    'Smoking_Habit': [smoking_habit],
    'Work_Hours': [work_hours],
    'Travel_Time': [travel_time],
    'Social_Interactions': [social_interactions],
    'Blood_Pressure': [blood_pressure],
    'Cholesterol_Level': [cholesterol_level],
    'Blood_Sugar_Level': [blood_sugar_level]
})

# Make prediction
if st.button("🔮 Predict Stress Level", key="predict_btn"):
    try:
        # Get prediction and probability
        prediction = model.predict(input_data)
        pred_value = prediction[0]
        
        # Get probabilities for all classes [0, 1, 2]
        probabilities = model.predict_proba(input_data)[0]
        
        # Calculate weighted stress percentage
        # Class 0 = No Stress (0%), Class 1 = Moderate (50%), Class 2 = High Stress (100%)
        stress_percentage = (probabilities[0] * 0 + probabilities[1] * 50 + probabilities[2] * 100)
        
        # Determine status based on prediction
        if pred_value == 0:
            stress_status = "🟢 Low Stress - You're doing great!"
            status_color = "#28a745"
        elif pred_value == 1:
            stress_status = "🟡 Moderate Stress - Consider some relaxation"
            status_color = "#ffc107"
        else:  # pred_value == 2
            stress_status = "🔴 High Stress - Please take care of yourself"
            status_color = "#dc3545"
        
        # Display results
        st.success("✅ Prediction Complete!")
        
        # Main stress indicator
        st.subheader("Stress Level Assessment")
        st.markdown(f"### {stress_status}")
        st.progress(stress_percentage / 100)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Stress Percentage", f"{stress_percentage:.1f}%")
        with col2:
            if pred_value == 0:
                classification = "No Stress"
            elif pred_value == 1:
                classification = "Moderate Stress"
            else:
                classification = "High Stress"
            st.metric("Classification", classification)
        with col3:
            st.metric("Stress Level", f"Level {pred_value}")
        
        # Visual chart
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = stress_percentage,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Stress Level", 'font': {'size': 24}},
            gauge = {
                'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
                'bar': {'color': status_color},
                'bgcolor': "white",
                'borderwidth': 2,
                'bordercolor': "gray",
                'steps': [
                    {'range': [0, 50], 'color': '#d4edda'},
                    {'range': [50, 100], 'color': '#f8d7da'}],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 70}}))
        
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
        
        # Show input summary
        with st.expander("📊 View Input Summary"):
            st.dataframe(input_data.T)
        
    except Exception as e:
        st.error(f"Error making prediction: {str(e)}")

# Sidebar info
st.sidebar.title("About")
st.sidebar.info("""
**Stress Detection Predictor**

This model uses a Support Vector Classifier trained on health metrics and lifestyle factors to predict stress levels.

**Features used:**
- Age, Blood Pressure, Cholesterol, Blood Sugar Level
- Work Hours, Sleep Duration, Sleep Quality
- Physical Activity, Screen Time
- Caffeine Intake, Alcohol Intake
- Social Interactions, Smoking Habit
- Travel Time
""")
