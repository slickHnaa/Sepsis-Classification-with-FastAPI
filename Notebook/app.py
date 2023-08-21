from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from imblearn.over_sampling import SMOTE
import joblib

app = FastAPI(debug=True)

# Load pre-trained models and transformers
label_encoder = joblib.load("label_encoder.joblib")
numerical_imputer = joblib.load("numerical_imputer.joblib")
scaler = joblib.load("scaler.joblib")
smote = SMOTE()

class SepsisPredictionInput(BaseModel):
    Age: float
    Temperature: float
    HeartRate: float
    BloodPressure: float
    PRG: float 
    PR: float         
    SK: float          
    TS: float           
    M11: float        
    BD2: float        
    Age: float         
    Insurance: float

@app.post("/predict/")
async def predict_sepsis(sepsis_data: SepsisPredictionInput):
    # Convert the incoming data to a DataFrame
    input_data = pd.DataFrame([sepsis_data.dict()])

    # Impute missing values
    input_imputed = numerical_imputer.transform(input_data)

    # Scale the input data
    input_scaled = scaler.transform(input_imputed)

    # Predict sepsis using a trained model (replace 'model' with your actual model)
    prediction = model.predict(input_scaled)

    # Convert prediction to human-readable label
    predicted_label = label_encoder.inverse_transform(prediction)[0]

    return {"predicted_sepsis": predicted_label}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
