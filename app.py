from flask import Flask, render_template, request, jsonify
from together import Together
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
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

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate-plan", methods=["POST"])
def generate_plan():
    try:
        data = request.json
        diet_plan = generate_diet_plan_stream(
            height=data["height"],
            weight=data["weight"],
            age=data["age"],
            gender=data["gender"],
            activity_level=data["activity_level"],
            goals=data["goals"]
        )
        return jsonify({"diet_plan": diet_plan})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
