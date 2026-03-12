from fastapi import FastAPI
import joblib
import numpy as np
import pandas as pd

app = FastAPI()

# Load ML model
model = joblib.load("C:\\Projects\\MetaLearn\\Models\\model.pkl")

# Load questions dataset
questions = pd.read_csv("C:\\Projects\\MetaLearn\\Dataset\\questions.csv")


@app.get("/")
def home():
    return {"message": "MetaLearn API running"}


@app.post("/predict")
def predict_mastery(accuracy: float, time_score: float, confidence: float, attempt: float):

    # Prepare input
    input_data = np.array([[accuracy, time_score, confidence, attempt]])

    # Predict mastery
    prediction = model.predict(input_data)[0]

    # Decide difficulty
    if prediction > 0.8:
        recommendation = "harder question"
        difficulty = "hard"
    elif prediction > 0.5:
        recommendation = "same difficulty"
        difficulty = "medium"
    else:
        recommendation = "easier question"
        difficulty = "easy"

    # Filter questions by difficulty
    filtered = questions[questions["difficulty"] == difficulty]

    if filtered.empty:
        return {
            "mastery_score": float(prediction),
            "recommendation": recommendation,
            "message": "No questions available for this difficulty"
        }

    # Select random question
    q = filtered.sample(1).iloc[0]

    return {
        "mastery_score": float(prediction),
        "recommendation": recommendation,
        "difficulty": difficulty,
        "question": q["question_text"],
        "options": {
            "A": q["option_a"],
            "B": q["option_b"],
            "C": q["option_c"],
            "D": q["option_d"]
        }
    }