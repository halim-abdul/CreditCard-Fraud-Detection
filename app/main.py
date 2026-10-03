import os
import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from app.schemas import Transaction, Prediction
from src.risk import risk_band, risk_score

MODEL_PATH = os.getenv("MODEL_PATH", "models/model.joblib")
app = FastAPI(title="Credit Card Fraud Detection API", version="1.0.0")
model = None

@app.on_event("startup")
def load_model():
    global model
    if os.path.exists(MODEL_PATH):
        model = joblib.load(MODEL_PATH)

@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": model is not None}

@app.post("/predict", response_model=Prediction)
def predict(tx: Transaction):
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    X = pd.DataFrame([tx.features])
    p = float(model.predict_proba(X)[0, 1])
    return Prediction(fraud_probability=p, risk_score=risk_score(p), risk_band=risk_band(p))
