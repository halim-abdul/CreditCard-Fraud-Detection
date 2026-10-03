from sklearn.calibration import CalibratedClassifierCV


def calibrated_model(estimator, method: str = "isotonic", cv: int = 3):
    return CalibratedClassifierCV(estimator=estimator, method=method, cv=cv)
