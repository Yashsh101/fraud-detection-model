from src.data import FEATURE_COLUMNS, make_synthetic_transactions
from src.model import evaluate_model, train_model


def test_synthetic_dataset_has_expected_columns_and_imbalance():
    df = make_synthetic_transactions(n_samples=300, random_state=7)

    assert set(FEATURE_COLUMNS + ["is_fraud"]).issubset(df.columns)
    assert 0 < df["is_fraud"].mean() < 0.2


def test_model_trains_and_returns_metrics():
    df = make_synthetic_transactions(n_samples=500, random_state=7)
    model, x_test, y_test = train_model(df, random_state=7)
    metrics = evaluate_model(model, x_test, y_test)

    assert 0 <= metrics["recall"] <= 1
    assert 0 <= metrics["precision"] <= 1
    assert 0 <= metrics["roc_auc"] <= 1
