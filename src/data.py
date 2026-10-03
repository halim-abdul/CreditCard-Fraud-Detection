from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split


def load_transactions(path: str | Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    if "Class" not in df.columns:
        raise ValueError("Expected binary target column 'Class'.")
    return df


def stratified_split(df: pd.DataFrame, target: str = "Class", test_size: float = 0.2, random_state: int = 42):
    X = df.drop(columns=[target])
    y = df[target].astype(int)
    return train_test_split(X, y, test_size=test_size, stratify=y, random_state=random_state)
