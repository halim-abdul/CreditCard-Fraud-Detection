import argparse
import joblib
from pathlib import Path
from sklearn.metrics import average_precision_score
from src.data import load_transactions, stratified_split
from src.features import add_basic_features
from src.models import logistic_baseline


def main():
    p = argparse.ArgumentParser()
    p.add_argument("data")
    p.add_argument("--output", default="models/logistic.joblib")
    args = p.parse_args()

    df = add_basic_features(load_transactions(args.data))
    X_train, X_test, y_train, y_test = stratified_split(df)
    model = logistic_baseline()
    model.fit(X_train, y_train)
    score = average_precision_score(y_test, model.predict_proba(X_test)[:, 1])
    print(f"PR-AUC={score:.6f}")
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, args.output)


if __name__ == "__main__":
    main()
