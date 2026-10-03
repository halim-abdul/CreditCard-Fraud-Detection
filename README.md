# CreditCard-Fraud-Detection

An end-to-end machine-learning framework for credit-card fraud detection using XGBoost and LightGBM, class-imbalance mitigation, robust feature engineering, hyperparameter optimization, explainable AI, calibrated probabilistic risk scoring, threshold tuning, and production-oriented evaluation.

## Project goals

This repository grows from a simple reproducible baseline into an advanced fraud analytics system. It is designed for rare-event classification where accuracy alone is misleading and operational costs matter.

## Roadmap

1. **Data foundations** — schema checks, leakage prevention, stratified and temporal splits.
2. **Feature engineering** — amount/time transformations, velocity features, robust preprocessing.
3. **Modeling** — Logistic Regression baseline, XGBoost, LightGBM, imbalance strategies, Optuna.
4. **Evaluation & XAI** — PR-AUC, ROC-AUC, calibration, threshold tuning, SHAP, cost analysis.
5. **Real-time & MLOps** — risk scoring API, monitoring, drift checks, testing, reproducibility.

## Repository structure

```text
src/        reusable Python modules
docs/       technique and design notes
scripts/    command-line training/evaluation utilities
configs/    experiment configuration
tests/      unit tests
data/       local data placeholders
models/     generated model artifacts (ignored)
```

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Place a dataset containing a binary `Class` target in `data/raw/`, then use the modules under `src/` to construct train/validation/test workflows.

## Evaluation philosophy

For highly imbalanced fraud data, prioritize **precision-recall metrics, recall at controlled false-positive rates, probability calibration, cost-sensitive thresholding, and temporal validation**. Always compare against simple baselines and guard against data leakage.

## License

Released under the repository's existing MIT License.
