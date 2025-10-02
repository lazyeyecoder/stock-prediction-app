from fastapi import FastAPI
from pydantic import BaseModel
import joblib

#loading the trained model which was downloaded as pkl from google colab
model = joblib.load("model.pkl")

class InputData(BaseModel):
  AdjClose: float
  MA5: float
  MA10: float

app = FastAPI()

@app.get("/") #to test if server is live
def home():
  return {"message" : "Stock Prediction API is running!"}

@app.post("/predict") #takes a number and predicts 1 or 0 (buy or sell)
def predict(data: InputData):
  features = [[data.AdjClose, data.MA5, data.MA10]]
  prediction = model.predict(features)[0]
  return {"prediction": int(prediction)}
