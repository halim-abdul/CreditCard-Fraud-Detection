import numpy as np
from src.thresholds import expected_cost


def test_expected_cost_penalizes_missed_fraud():
    y = np.array([0, 1])
    p = np.array([0.1, 0.4])
    assert expected_cost(y, p, 0.5, 1.0, 10.0) == 10.0
