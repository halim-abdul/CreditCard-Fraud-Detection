import argparse
from pathlib import Path
import pandas as pd
from src.features import add_basic_features


def main():
    p = argparse.ArgumentParser()
    p.add_argument("input")
    p.add_argument("output")
    args = p.parse_args()
    df = pd.read_csv(args.input)
    out = add_basic_features(df)
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.output, index=False)


if __name__ == "__main__":
    main()
