# Model Card Template

## Intended use
Real-time or batch fraud-risk prioritization for credit-card transactions.

## Inputs
Document every feature, unit, availability time, and preprocessing rule.

## Outputs
Fraud probability, risk score, risk band, and optional analyst explanation.

## Evaluation
Report class prevalence, temporal window, PR-AUC, ROC-AUC, precision, recall, threshold, calibration, and error costs.

## Limitations
Performance may degrade under merchant/customer drift, new fraud patterns, label delay, or changes in authorization policy. Predictions should support risk controls and investigation rather than be interpreted as causal evidence.
