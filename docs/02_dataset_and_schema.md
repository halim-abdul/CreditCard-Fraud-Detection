# Dataset and Schema

A common public benchmark stores anonymized PCA-like variables `V1...V28`, plus `Time`, `Amount`, and binary target `Class` where fraud is the minority class.

## Data contract
- `Class`: 0 legitimate, 1 fraud.
- numerical predictors must be finite at inference time;
- never train on identifiers or labels unavailable at authorization time;
- preserve timestamps when a temporal split is possible.

## Validation checks
- duplicate rows;
- missing and infinite values;
- target prevalence;
- extreme transaction amounts;
- train/validation distribution drift.
