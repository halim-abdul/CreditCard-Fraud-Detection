import numpy as np
import pandas as pd


def validate_frame(df: pd.DataFrame, target: str = "Class") -> dict:
    if target not in df:
        raise ValueError(f"Missing target column: {target}")
    numeric = df.select_dtypes(include=[np.number])
    return {
        "rows": int(len(df)),
        "columns": int(df.shape[1]),
        "missing": int(df.isna().sum().sum()),
        "infinite": int(np.isinf(numeric.to_numpy()).sum()),
        "fraud_rate": float(df[target].mean()),
        "duplicates": int(df.duplicated().sum()),
    }
