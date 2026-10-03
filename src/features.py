import numpy as np
import pandas as pd


def add_basic_features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    if "Amount" in out:
        out["Amount_log1p"] = np.log1p(out["Amount"].clip(lower=0))
        out["Amount_sqrt"] = np.sqrt(out["Amount"].clip(lower=0))
    if "Time" in out:
        seconds_day = 24 * 3600
        phase = 2 * np.pi * (out["Time"] % seconds_day) / seconds_day
        out["Time_sin"] = np.sin(phase)
        out["Time_cos"] = np.cos(phase)
    return out
