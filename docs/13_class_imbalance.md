# Class Imbalance

Fraud is a rare-event problem, so a model can achieve high accuracy while missing almost every fraud case.

Useful strategies include class weighting, threshold tuning, carefully applied undersampling/oversampling, and evaluation with precision-recall metrics. Never resample validation or test data. If SMOTE is used, place it inside the training pipeline/fold only.
