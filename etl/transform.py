# """Light transform placeholder: reads data/sample.csv and returns a simple summary."""
# import pandas as pd
# from pathlib import Path

# def summarize(path=None):
#     p = Path(path) if path else Path(__file__).resolve().parent.parent / "data" / "sample.csv"
#     df = pd.read_csv(p)
#     return {"rows": len(df), "sum": int(df['value'].sum())}

# if __name__ == "__main__":
#     print(summarize())

import pandas as pd
import pathlib

RAW_PATH = pathlib.Path("data/sample.csv")
STAGED_PATH = pathlib.Path("data/staged.parquet")

def clean_data():
    df = pd.read_csv(RAW_PATH)

    # Standardize col names
    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    # Basic cleaning assumptions — adjust for your dataset
    # Convert date column
    date_cols = [c for c in df.columns if "date" in c]
    if date_cols:
        df[date_cols[0]] = pd.to_datetime(df[date_cols[0]], errors="coerce")

    # Drop rows with no county or date
    key_cols = ["county", date_cols[0]] if date_cols else []
    for col in key_cols:
        if col in df.columns:
            df = df.dropna(subset=[col])

    # Output to parquet
    STAGED_PATH.parent.mkdir(exist_ok=True)
    df.to_parquet(STAGED_PATH, index=False)
    print("Staged data saved:", STAGED_PATH)

if __name__ == "__main__":
    clean_data()
