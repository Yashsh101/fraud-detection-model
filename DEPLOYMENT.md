# Deployment

This repo should not be deployed as a flagship project yet. It is now structured so it can be deployed after the dataset and evaluation story are improved.

## Local API

Train first:

```bash
python scripts/train.py
```

Run:

```bash
uvicorn app.api:app --host 0.0.0.0 --port 8000
```

## Future Render or Railway Plan

1. Add a Dockerfile or platform start command.
2. Train the model during build only if the dataset is small and reproducible.
3. Prefer storing a versioned model artifact externally for real projects.
4. Set environment variables from `.env.example`.
5. Verify `/health` and `/predict`.

## Production Checklist Before Public Demo

- Replace synthetic data with a cited public dataset.
- Add an evaluation report committed under `docs/`.
- Add model comparison and threshold tuning.
- Add explainability.
- Add Dockerfile.
