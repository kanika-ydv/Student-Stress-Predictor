from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
import tensorflow as tf
import pickle

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = tf.keras.models.load_model('stress_model.h5')
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

class UserInput(BaseModel):
    features: list[float] 

@app.post("/predict")
def predict_stress(data: UserInput):
    try:
        input_data = np.array(data.features).reshape(1, -1)
        scaled_data = scaler.transform(input_data)
        prediction = model.predict(scaled_data)
        predicted_class = int(np.argmax(prediction, axis=1)[0])
        
        levels = {0: "Low", 1: "Medium", 2: "High"}
        return {"stress_level": levels.get(predicted_class, "Unknown")}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
