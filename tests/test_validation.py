import pandas as pd
from src.validation import validate_frame


def test_validate_frame_counts_fraud():
    df = pd.DataFrame({"x": [1.0, 2.0, 3.0], "Class": [0, 1, 0]})
    result = validate_frame(df)
    assert result["rows"] == 3
    assert result["fraud_rate"] == 1 / 3
