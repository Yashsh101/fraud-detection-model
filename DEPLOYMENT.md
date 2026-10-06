# Deployment

This repository is a local demonstration using synthetic data. Do not use it for real financial decisions or deploy it as a hosted decisioning service without addressing the limitations in `MODEL_CARD.md`.

## Local API

Train first:

```bash
python -m scripts.train
```

Run:

```bash
uvicorn app.api:app --host 0.0.0.0 --port 8000
```

## Future Hosted Demo Considerations

1. Use the included Dockerfile or a platform start command.
2. Train the model during build only if the dataset is small and reproducible.
3. Prefer storing a versioned model artifact externally for real projects.
4. Export environment variables documented in `.env.example` before starting the process.
5. Verify `/health` and `/predict`.

## Additional Work Before Any Public Demo

- Replace synthetic data with a cited public dataset.
- Add an evaluation report committed under `docs/`.
- Add model comparison and threshold tuning.
- Add explainability.
- Add Dockerfile.
