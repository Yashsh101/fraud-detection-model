from __future__ import annotations

import numpy as np
import pandas as pd


FEATURE_COLUMNS = [
    "amount",
    "hour",
    "merchant_risk",
    "customer_age_days",
    "transactions_last_24h",
    "is_foreign",
]


def make_synthetic_transactions(n_samples: int = 2500, random_state: int = 42) -> pd.DataFrame:
    """Create a small imbalanced fraud-like dataset for reproducible demos."""
    rng = np.random.default_rng(random_state)

    amount = rng.lognormal(mean=4.4, sigma=1.0, size=n_samples)
    hour = rng.integers(0, 24, size=n_samples)
    merchant_risk = rng.beta(2, 5, size=n_samples)
    customer_age_days = rng.integers(1, 2500, size=n_samples)
    transactions_last_24h = rng.poisson(2, size=n_samples)
    is_foreign = rng.binomial(1, 0.12, size=n_samples)

    risk = (
        0.018 * np.log1p(amount)
        + 0.95 * merchant_risk
        + 0.10 * transactions_last_24h
        + 0.65 * is_foreign
        + np.where((hour <= 4) | (hour >= 23), 0.55, 0.0)
        + np.where(customer_age_days < 30, 0.55, 0.0)
        + rng.normal(0, 0.35, size=n_samples)
    )
    threshold = np.quantile(risk, 0.93)
    is_fraud = (risk >= threshold).astype(int)

    return pd.DataFrame(
        {
            "amount": amount.round(2),
            "hour": hour,
            "merchant_risk": merchant_risk.round(3),
            "customer_age_days": customer_age_days,
            "transactions_last_24h": transactions_last_24h,
            "is_foreign": is_foreign,
            "is_fraud": is_fraud,
        }
    )
