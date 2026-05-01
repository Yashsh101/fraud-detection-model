import json
from pathlib import Path

from src.data import make_synthetic_transactions
from src.model import evaluate_model, save_model, train_model
from src.settings import settings


def main() -> None:
    df = make_synthetic_transactions(random_state=settings.random_state)
    model, x_test, y_test = train_model(df, random_state=settings.random_state)
    metrics = evaluate_model(model, x_test, y_test, threshold=settings.fraud_threshold)

    save_model(model, settings.model_path)
    report_path = Path(settings.report_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(metrics, indent=2), encoding="utf-8")

    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
