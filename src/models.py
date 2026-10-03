from sklearn.linear_model import LogisticRegression


def logistic_baseline(random_state: int = 42):
    return LogisticRegression(
        class_weight="balanced",
        max_iter=2000,
        random_state=random_state,
    )


def xgboost_model(random_state: int = 42, scale_pos_weight: float = 1.0):
    from xgboost import XGBClassifier
    return XGBClassifier(
        n_estimators=400,
        learning_rate=0.05,
        max_depth=5,
        subsample=0.9,
        colsample_bytree=0.9,
        eval_metric="logloss",
        scale_pos_weight=scale_pos_weight,
        random_state=random_state,
    )


def lightgbm_model(random_state: int = 42, scale_pos_weight: float = 1.0):
    from lightgbm import LGBMClassifier
    return LGBMClassifier(
        n_estimators=400,
        learning_rate=0.05,
        num_leaves=31,
        subsample=0.9,
        colsample_bytree=0.9,
        scale_pos_weight=scale_pos_weight,
        random_state=random_state,
        verbosity=-1,
    )
