import json
from pathlib import Path

from src.data import make_synthetic_transactions
from src.model import evaluate_model, load_model
from src.settings import settings


def main() -> None:
    model_path = Path(settings.model_path)
    if not model_path.exists():
        raise SystemExit("Model artifact not found. Run `python scripts/train.py` first.")

    df = make_synthetic_transactions(random_state=settings.random_state)
    x = df.drop(columns=["is_fraud"])
    y = df["is_fraud"]
    model = load_model(settings.model_path)
    metrics = evaluate_model(model, x, y, threshold=settings.fraud_threshold)
    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
