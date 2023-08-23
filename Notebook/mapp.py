from fastapi import FastAPI, HTTPException
import joblib
from pydantic import BaseModel
import uvicorn
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from imblearn.over_sampling import SMOTE


app = FastAPI(debug=True)


#Load pre-trained models and transformers
label_encoder = joblib.load(r'C:\Users\user\Documents\AzubiAfrica\LP6\Sepsis-Classification-with-FastAPI\Notebook\Assets\label_encoder.joblib')
numerical_imputer = joblib.load(r'C:\Users\user\Documents\AzubiAfrica\LP6\Sepsis-Classification-with-FastAPI\Notebook\Assets\numerical_imputer.joblib')
scaler = joblib.load(r'C:\Users\user\Documents\AzubiAfrica\LP6\Sepsis-Classification-with-FastAPI\Notebook\Assets\scaler.joblib')
model = joblib.load(r'C:\Users\user\Documents\AzubiAfrica\LP6\Sepsis-Classification-with-FastAPI\Notebook\Assets\Final_model.joblib')
smote = SMOTE()





@app.get('/')
def predict_sepsis(PRG: float, PL: float, PR: float, SK: float,
          TS: float,  M11: float, BD2: float, Age: float, Insurance: int):

  
    sepsis_data = {
            'PRG': [PRG],
            'PL': [PL],
            'PR': [PR],
            'SK': [SK],
            'TS': [TS],
            'M11': [M11],
            'BD2': [BD2],
            'Age': [Age],
            'Insurance': [Insurance]
            } 


     
    #  Convert the incoming data to a DataFrame
    input_data = pd.DataFrame([sepsis_data.dict()])

    # Impute missing values
    input_imputed = numerical_imputer.transform(input_data)

    # Scale the input data
    input_scaled = scaler.transform(input_imputed)

    # Predict sepsis using a trained model (replace 'model' with your actual model)
    prediction = model.predict(input_scaled)

    # Convert prediction to human-readable label
    predicted_label = label_encoder.inverse_transform(prediction)[0]

    probabilities = model.predict_proba(input_scaled)[0]
    prediction = np.argmax(probabilities)

    sepsis_status = "Positive" if prediction == 1 else "Negative"
    
    probability = probabilities[1] if prediction == 1 else probabilities[0]

    #statement = f"The patient is {sepsis_status}. There is a {'high' if prediction == 1 else 'low'} probability ({probability:.2f}) that the patient is susceptible to developing sepsis."

    if prediction == 1:
        status_icon = "✔"  # Red 'X' icon for positive sepsis prediction
        sepsis_explanation = "Sepsis is a life-threatening condition caused by an infection. A positive prediction suggests that the patient might be exhibiting sepsis symptoms and requires immediate medical attention."
    else:
        status_icon = "✘"  # Green checkmark icon for negative sepsis prediction
        sepsis_explanation = "Sepsis is a life-threatening condition caused by an infection. A negative prediction suggests that the patient is not currently exhibiting sepsis symptoms."

    statement = f"The patient's sepsis status is {sepsis_status} {status_icon} with a probability of {probability:.2f}. {sepsis_explanation}"

    user_input_statement = "Please note this is the user-inputted data: "

    output_df = pd.DataFrame([input_data])

    result = {'predicted_sepsis': sepsis_status, 'statement': statement, 'user_input_statement': user_input_statement, 'input_data_df': output_df.to_dict('records')}

    return result

if __name__ == "__main__":
  uvicorn.run(app)

