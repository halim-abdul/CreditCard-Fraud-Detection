# Feature Selection

Feature selection should improve generalization, speed, and interpretability rather than chase tiny validation gains.

Start with domain filtering and leakage removal. Then inspect permutation importance, SHAP stability, redundancy/correlation, and cross-validated ablations. For tree ensembles, do not treat built-in split importance as causal evidence.
