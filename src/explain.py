def shap_values(model, X):
    import shap
    explainer = shap.TreeExplainer(model)
    return explainer(X)
