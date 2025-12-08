# etl/transform.py
# Light transform helpers: summarize (small) and clean_data (staging/parquet)

import pandas as pd
import pathlib
from pathlib import Path
from typing import Optional, Dict, Any

RAW_PATH = pathlib.Path("data/sample.csv")
STAGED_PATH = pathlib.Path("data/staged.parquet")

def summarize(path: Optional[str] = None) -> Dict[str, Any]:
    """
    Read a small CSV and return a simple summary dictionary.
    Keeps backwards-compatible behavior used by tests:
      {"rows": <int>, "sum": <int>}  # sum is of 'value' column if present, else 0
    """
    p = Path(path) if path else RAW_PATH
    if not p.exists():
        return {"rows": 0, "sum": 0}

    df = pd.read_csv(p)
    rows = len(df)
    total = int(df["value"].sum()) if "value" in df.columns else 0
    return {"rows": rows, "sum": total}

def clean_data():
    """
    Read RAW_PATH, do light cleaning and normalization, and write STAGED_PATH parquet.
    This function intentionally writes parquet; if running locally ensure pyarrow or fastparquet is installed.
    """
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

    # Drop rows with no county or date (if date column detected)
    key_cols = ["county", date_cols[0]] if date_cols else []
    for col in key_cols:
        if col in df.columns:
            df = df.dropna(subset=[col])

    # Output to parquet
    STAGED_PATH.parent.mkdir(exist_ok=True)
    df.to_parquet(STAGED_PATH, index=False)
    print("Staged data saved:", STAGED_PATH)

if __name__ == "__main__":
    # keep the module runnable for quick manual checks
    print("Summary:", summarize())
    # Note: avoid calling clean_data() automatically to prevent parquet errors in environments missing pyarrow