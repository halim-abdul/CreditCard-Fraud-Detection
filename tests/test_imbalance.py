import numpy as np
from src.imbalance import positive_class_weight


def test_positive_class_weight():
    y = np.array([0, 0, 0, 1])
    assert positive_class_weight(y) == 3.0
