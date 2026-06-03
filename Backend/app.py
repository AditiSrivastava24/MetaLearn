from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
import numpy as np
import pandas as pd

app = FastAPI()

# Enable CORS so frontend can access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load ML model
model = joblib.load("C:\\Projects\\MetaLearn\\Models\\model.pkl")

# Load questions dataset
questions = pd.read_csv("C:\\Projects\\MetaLearn\\Dataset\\questions.csv")


@app.get("/")
def home():
    return {"message": "MetaLearn API running"}


# Get question by difficulty
@app.get("/question")
def get_question(difficulty: str):

    filtered = questions[questions["difficulty"] == difficulty]

    if filtered.empty:
        return {"error": "No questions found"}

    q = filtered.sample(1).iloc[0]

    return {
        "question_id": int(q["question_id"]),
        "question": q["question_text"],
        "options": {
            "A": q["option_a"],
            "B": q["option_b"],
            "C": q["option_c"],
            "D": q["option_d"]
        },
        "correct_answer": q["correct_answer"]
    }


# Predict mastery and recommend next difficulty
@app.post("/predict")
def predict_mastery(accuracy: float, time_score: float, confidence: float, attempt: float):

    input_data = np.array([[accuracy, time_score, confidence, attempt]])

    prediction = model.predict(input_data)[0]

    if prediction > 0.8:
        recommendation = "harder question"
        difficulty = "hard"
    elif prediction > 0.5:
        recommendation = "same difficulty"
        difficulty = "medium"
    else:
        recommendation = "easier question"
        difficulty = "easy"

    return {
        "mastery_score": float(prediction),
        "recommendation": recommendation,
        "next_difficulty": difficulty
    }