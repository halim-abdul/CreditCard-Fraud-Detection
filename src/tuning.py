def xgb_objective(trial, X_train, y_train, X_valid, y_valid):
    from sklearn.metrics import average_precision_score
    from xgboost import XGBClassifier

    model = XGBClassifier(
        n_estimators=trial.suggest_int("n_estimators", 200, 700),
        max_depth=trial.suggest_int("max_depth", 3, 8),
        learning_rate=trial.suggest_float("learning_rate", 0.01, 0.2, log=True),
        subsample=trial.suggest_float("subsample", 0.6, 1.0),
        colsample_bytree=trial.suggest_float("colsample_bytree", 0.6, 1.0),
        eval_metric="logloss",
        random_state=42,
    )
    model.fit(X_train, y_train)
    p = model.predict_proba(X_valid)[:, 1]
    return average_precision_score(y_valid, p)
