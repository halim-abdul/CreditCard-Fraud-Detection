import pandas as pd
from src.features import add_basic_features


def test_add_basic_features():
    df = pd.DataFrame({"Amount": [0.0, 99.0], "Time": [0.0, 3600.0]})
    out = add_basic_features(df)
    assert {"Amount_log1p", "Amount_sqrt", "Time_sin", "Time_cos"}.issubset(out.columns)
    assert len(out) == 2
