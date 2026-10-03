# Deployment Guide

1. Train and validate the model offline.
2. Freeze preprocessing, model artifact, threshold, and feature schema.
3. Build the container image.
4. Inject `MODEL_PATH` through environment configuration.
5. Run smoke tests against `/health` and `/predict`.
6. Deploy behind authentication, TLS, rate limits, and observability.
7. Monitor latency, errors, score drift, feature drift, and delayed-label quality.

Use canary or shadow evaluation when replacing an existing production model.
