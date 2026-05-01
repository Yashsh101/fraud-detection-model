from pathlib import Path

import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from src.data import FEATURE_COLUMNS
from src.model import load_model
from src.settings import settings


class Transaction(BaseModel):
    amount: float = Field(..., ge=0)
    hour: int = Field(..., ge=0, le=23)
    merchant_risk: float = Field(..., ge=0, le=1)
    customer_age_days: int = Field(..., ge=0)
    transactions_last_24h: int = Field(..., ge=0)
    is_foreign: bool = False


app = FastAPI(
    title="Fraud Detection API",
    version="0.2.0",
    description="Lightweight fraud-risk inference API for portfolio demonstration.",
)


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "model_available": Path(settings.model_path).exists()}


@app.post("/predict")
def predict(transaction: Transaction) -> dict:
    if not Path(settings.model_path).exists():
        raise HTTPException(status_code=503, detail="Model artifact not found. Run training first.")

    model = load_model(settings.model_path)
    row = pd.DataFrame([{column: getattr(transaction, column) for column in FEATURE_COLUMNS}])
    row["is_foreign"] = row["is_foreign"].astype(int)
    probability = float(model.predict_proba(row)[0, 1])
    requires_review = probability >= settings.fraud_threshold

    return {
        "fraud_probability": round(probability, 4),
        "threshold": settings.fraud_threshold,
        "decision": "manual_review" if requires_review else "approve",
        "requires_review": requires_review,
    }
