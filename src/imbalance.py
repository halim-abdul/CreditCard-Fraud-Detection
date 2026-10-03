import numpy as np


def positive_class_weight(y) -> float:
    y = np.asarray(y)
    positives = max(int((y == 1).sum()), 1)
    negatives = int((y == 0).sum())
    return negatives / positives
