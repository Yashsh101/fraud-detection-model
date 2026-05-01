# Model Card: Fraud Detection Scaffold

## Model Details

- Task: Binary classification for fraud-risk review.
- Current data: Synthetic imbalanced transaction-like records.
- Model: Logistic Regression with class weighting.
- Features: amount, transaction hour, merchant risk, customer age, recent transaction count, foreign transaction flag.
- Output: Fraud probability and manual-review decision.

## Intended Use

This is an early ML project and educational scaffold. It demonstrates a clean training/evaluation/API structure for fraud detection, but it is not ready for production financial decisions.

## Evaluation

The scripts report precision, recall, F1, ROC-AUC, and confusion matrix. In fraud workflows, recall matters because false negatives are costly. Precision also matters because too many false positives overwhelm review teams.

## Limitations

- Uses synthetic data, not real fraud transactions.
- Does not include time-based validation.
- Does not include fraud-specific feature engineering from real payment systems.
- Does not include explainability or monitoring.
- Should not be used for real financial decisions.

## Next Improvements

- Use a cited public fraud dataset.
- Add threshold tuning based on review capacity.
- Compare Logistic Regression with tree-based models.
- Add feature importance or SHAP explanations.
- Add drift monitoring and retraining notes.
