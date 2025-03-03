import streamlit as st
from together import Together
import os
from dotenv import load_dotenv

load_dotenv()

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

# Initialize Together client
client = Together(api_key=TOGETHER_API_KEY)

def generate_diet_plan_stream(height, weight, age, gender, activity_level, goals):
    prompt = f"""
    Act as an expert on fitness, nutrition and training and
    Create a personalized diet plan for a {age}-year-old {gender}, 
    weighing {weight} kg, and {height} cm tall.
    Activity level: {activity_level}. Goals: {goals}.
    Provide a detailed meal plan for breakfast, lunch, dinner, and snacks.
    Include portion sizes and nutritional information but keep your answer brief.
    """
    
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1024,
        temperature=0.7,
        stream=True
    )
    
    full_response = []
    for chunk in response:
        if chunk.choices[0].delta.content:
            full_response.append(chunk.choices[0].delta.content)
    
    return "".join(full_response)

# Streamlit UI
st.title("Personalized Diet Plan Generator")

# User Inputs
height = st.number_input("Height (cm)", min_value=50, max_value=250)
weight = st.number_input("Weight (kg)", min_value=20, max_value=200)
age = st.number_input("Age", min_value=5, max_value=100)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
activity_level = st.selectbox("Activity Level", ["Sedentary", "Light", "Moderate", "Active", "Very Active"])
goals = st.text_area("Your Goals")

if st.button("Generate Diet Plan"):
    if height and weight and age and gender and activity_level and goals:
        with st.spinner("Generating diet plan..."):
            diet_plan = generate_diet_plan_stream(height, weight, age, gender, activity_level, goals)
        st.subheader("Your Personalized Diet Plan:")
        st.write(diet_plan)
    else:
        st.warning("Please fill in all fields.")
