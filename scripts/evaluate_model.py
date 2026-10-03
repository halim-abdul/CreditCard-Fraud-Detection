import argparse
import joblib
import pandas as pd
from src.metrics import classification_metrics


def main():
    p = argparse.ArgumentParser()
    p.add_argument("model")
    p.add_argument("data")
    p.add_argument("--target", default="Class")
    p.add_argument("--threshold", type=float, default=0.5)
    args = p.parse_args()

    model = joblib.load(args.model)
    df = pd.read_csv(args.data)
    y = df.pop(args.target).astype(int)
    proba = model.predict_proba(df)[:, 1]
    print(classification_metrics(y, proba, args.threshold))


if __name__ == "__main__":
    main()
