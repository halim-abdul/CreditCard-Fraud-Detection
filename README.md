# CreditCard-Fraud-Detection

An end-to-end machine-learning framework for credit-card fraud detection using **XGBoost, LightGBM, imbalance-aware training, robust feature engineering, hyperparameter optimization, explainable AI, calibrated probabilistic risk scoring, threshold tuning, and real-time serving**.

The repository is intentionally organized from simple to advanced so it can be used both as a learning project and as a production-oriented reference architecture.

## What is included

- data validation and leakage prevention;
- stratified and production-like temporal splitting guidance;
- amount, cyclic-time, robust and velocity feature engineering;
- Logistic Regression baseline;
- XGBoost and LightGBM model factories;
- class weighting, random over/undersampling, and SMOTE helpers;
- Optuna-ready hyperparameter optimization;
- PR-AUC, ROC-AUC, precision, recall and F1 evaluation;
- cost-sensitive threshold optimization;
- probability calibration;
- probabilistic risk scores and risk bands;
- SHAP explanation support;
- FastAPI real-time scoring service;
- PSI-style drift monitoring helper;
- Docker, tests, GitHub Actions and reproducibility guidance;
- extensive short Markdown notes explaining techniques and operational choices.

## Architecture

```text
Transaction data
     |
     v
Data validation + leakage controls
     |
     v
Feature engineering
(amount / time / robust / velocity)
     |
     v
Train / validation / test strategy
     |
     +-------------------------------+
     |                               |
Logistic baseline              XGBoost / LightGBM
                                     |
                              imbalance handling
                                     |
                              hyperparameter tuning
                                     |
                                     v
                           calibrated probability
                                     |
                         threshold + expected cost
                                     |
                                     v
                           risk score / risk band
                                     |
                      +--------------+-------------+
                      |                            |
                 SHAP analysis                FastAPI API
                                                   |
                                            monitoring/drift
```

## Repository structure

```text
app/         FastAPI scoring service and schemas
configs/     feature/model configuration examples
data/        local raw and processed data placeholders
docs/        technique, modeling, evaluation and MLOps notes
scripts/     feature building, training and evaluation commands
src/         reusable ML modules
tests/       unit tests
.github/     CI workflow
Dockerfile   API container
Makefile     common developer commands
```

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate          # Linux/macOS
# .venv\Scripts\activate           # Windows
pip install -r requirements.txt
pytest -q
```

Place a CSV with binary target `Class` in `data/raw/`. A common public benchmark uses numerical columns such as `Time`, `Amount`, anonymized `V1...V28`, and target `Class`.

Build basic engineered features:

```bash
python scripts/build_features.py data/raw/creditcard.csv data/processed/features.csv
```

Train the simple baseline:

```bash
python scripts/train_baseline.py data/processed/features.csv
```

## Real-time API

After placing a fitted model at `models/model.joblib`:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Endpoints:

- `GET /health` — service/model readiness;
- `POST /predict` — fraud probability, 0–1000 risk score and risk band.

Docker:

```bash
docker build -t fraud-detection .
docker run -p 8000:8000 -v "$PWD/models:/app/models" fraud-detection
```

## Evaluation philosophy

Fraud is a rare-event problem. Do **not** judge a model mainly by accuracy. Prefer precision-recall metrics, calibration, threshold-specific precision/recall, review workload, false-positive cost, missed-fraud cost, and temporal robustness. Keep the final test set untouched until model and threshold choices are complete.

## Suggested learning path

1. Read `docs/01_problem_framing.md` through the data/splitting notes.
2. Explore feature-engineering notes and `src/features.py`.
3. Train the Logistic Regression baseline.
4. Compare XGBoost and LightGBM with class weighting.
5. Study resampling and Optuna tuning.
6. Move to PR-AUC, calibration, threshold and cost analysis.
7. Inspect SHAP explanations and probabilistic risk scores.
8. Run the FastAPI service and study monitoring/drift documentation.

## Important production considerations

This repository is a research/engineering framework, not a drop-in payment authorization system. Production use requires organization-specific feature contracts, authentication, encrypted transport/storage, secret management, point-in-time feature correctness, model governance, latency/error budgets, delayed-label monitoring, incident response, and validated business-cost assumptions.

## License

Released under the repository's existing MIT License.
