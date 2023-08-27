from fastapi import FastAPI, HTTPException
import uvicorn
import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import joblib

app = FastAPI(debug=True)

def load_model():
    cwd = os.getcwd()
    destination = os.path.join(cwd, "Assets")

    imputer_filepath = os.path.join(destination, "numerical_imputer.joblib")
    scaler_filepath = os.path.join(destination, "scaler.joblib")
    model_filepath = os.path.join(destination, "Final_01_model.joblib")

    num_imputer = joblib.load(imputer_filepath)
    scaler = joblib.load(scaler_filepath)
    model = joblib.load(model_filepath)

    return num_imputer, scaler, model

numerical_imputer, scaler, model = load_model()

@app.get("/")
async def read_root():
    return {"message": "Welcome To The Sepsis Prediction API"}

@app.post("/predict_sepsis")
async def predict_sepsis(PRG: float, PL: float, PR: float, SK: float, TS: float, M11: float, BD2: float, Age: float, Insurance: int):
    sepsis_data = {
        'PRG': PRG,
        'PL': PL,
        'PR': PR,
        'SK': SK,
        'TS': TS,
        'M11': M11,
        'BD2': BD2,
        'Age': Age,
        'Insurance': Insurance
    }

    input_data = pd.DataFrame([sepsis_data])  # Create a DataFrame from the dictionary

    input_imputed = numerical_imputer.transform(input_data)
    input_scaled = scaler.transform(input_imputed)

    prediction = model.predict(input_scaled)

    sepsis_status = "Positive" if prediction == 1 else "Negative"

    probabilities = model.predict_proba(input_scaled)[0]
    probability = probabilities[1] if prediction == 1 else probabilities[0]

    if prediction == 1:
        status_icon = "✔"
        sepsis_explanation = "Sepsis is a life-threatening condition caused by an infection. A positive prediction suggests that the patient might be exhibiting sepsis symptoms and requires immediate medical attention."
    else:
        status_icon = "✘"
        sepsis_explanation = "Sepsis is a life-threatening condition caused by an infection. A negative prediction suggests that the patient is not currently exhibiting sepsis symptoms."

    statement = f"The patient's sepsis status is {sepsis_status} {status_icon} with a probability of {probability:.2f}. {sepsis_explanation}"

    user_input_statement = f"Please note this is the user-inputted data: {sepsis_data}"

    result = {
        'predicted_sepsis': sepsis_status,
        'statement': statement,
        'user_input_statement': user_input_statement,
        'probability': probability
    }

    return result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
