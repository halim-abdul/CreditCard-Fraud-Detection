import pandas as pd


def past_event_count(df: pd.DataFrame, entity: str, time_col: str, window: str = "1h") -> pd.Series:
    work = df[[entity, time_col]].copy()
    work[time_col] = pd.to_datetime(work[time_col])
    work = work.sort_values([entity, time_col])
    counts = work.groupby(entity, group_keys=False).rolling(window, on=time_col, closed="left").count()[entity]
    return counts.reindex(df.index).fillna(0)
