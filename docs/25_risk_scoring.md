# Probabilistic Risk Scoring

A risk score maps model probability into an operational scale while preserving monotonicity. Example: `score = round(1000 * probability)`.

Risk bands such as low/medium/high/critical can simplify routing, but their boundaries should be validated against workload, loss, calibration, and customer-friction constraints. Keep raw probability for auditability.
