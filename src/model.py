from __future__ import annotations

from pathlib import Path

import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, f1_score, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from src.data import FEATURE_COLUMNS


def build_pipeline(random_state: int = 42) -> Pipeline:
    return Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            (
                "classifier",
                LogisticRegression(
                    class_weight="balanced",
                    max_iter=1000,
                    random_state=random_state,
                ),
            ),
        ]
    )


def train_model(df: pd.DataFrame, random_state: int = 42) -> tuple[Pipeline, pd.DataFrame, pd.Series]:
    x = df[FEATURE_COLUMNS]
    y = df["is_fraud"]
    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=0.25,
        random_state=random_state,
        stratify=y,
    )
    model = build_pipeline(random_state=random_state)
    model.fit(x_train, y_train)
    return model, x_test, y_test


def evaluate_model(model: Pipeline, x_test: pd.DataFrame, y_test: pd.Series, threshold: float = 0.5) -> dict:
    probabilities = model.predict_proba(x_test)[:, 1]
    predictions = (probabilities >= threshold).astype(int)
    matrix = confusion_matrix(y_test, predictions).tolist()

    return {
        "precision": round(precision_score(y_test, predictions, zero_division=0), 4),
        "recall": round(recall_score(y_test, predictions, zero_division=0), 4),
        "f1": round(f1_score(y_test, predictions, zero_division=0), 4),
        "roc_auc": round(roc_auc_score(y_test, probabilities), 4),
        "confusion_matrix": matrix,
        "threshold": threshold,
        "test_rows": int(len(y_test)),
    }


def save_model(model: Pipeline, path: str) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, target)


def load_model(path: str) -> Pipeline:
    return joblib.load(path)
