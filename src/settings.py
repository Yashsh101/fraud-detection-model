import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    model_path: str = os.getenv("MODEL_PATH", "artifacts/fraud_model.joblib")
    report_path: str = os.getenv("REPORT_PATH", "artifacts/evaluation.json")
    fraud_threshold: float = float(os.getenv("FRAUD_THRESHOLD", "0.50"))
    random_state: int = int(os.getenv("RANDOM_STATE", "42"))


settings = Settings()
