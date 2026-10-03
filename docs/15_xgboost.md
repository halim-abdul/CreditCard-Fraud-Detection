# XGBoost for Fraud Detection

XGBoost handles nonlinear interactions and heterogeneous numerical signals well. Important controls include tree depth, learning rate, number of trees, row/column subsampling, regularization, and `scale_pos_weight`.

Use validation PR-AUC or a business-aligned metric for tuning; do not optimize plain accuracy on highly imbalanced data.
