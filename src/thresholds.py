import numpy as np
from sklearn.metrics import confusion_matrix


def expected_cost(y_true, proba, threshold, false_positive_cost=1.0, false_negative_cost=10.0):
    pred = (proba >= threshold).astype(int)
    tn, fp, fn, tp = confusion_matrix(y_true, pred, labels=[0, 1]).ravel()
    return fp * false_positive_cost + fn * false_negative_cost


def best_cost_threshold(y_true, proba, false_positive_cost=1.0, false_negative_cost=10.0, grid=None):
    grid = np.linspace(0.01, 0.99, 99) if grid is None else grid
    scored = [(t, expected_cost(y_true, proba, t, false_positive_cost, false_negative_cost)) for t in grid]
    return min(scored, key=lambda x: x[1])
