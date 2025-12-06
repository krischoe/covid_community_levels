"""Light transform placeholder: reads data/sample.csv and returns a simple summary."""
import pandas as pd
from pathlib import Path

def summarize(path=None):
    p = Path(path) if path else Path(__file__).resolve().parent.parent / "data" / "sample.csv"
    df = pd.read_csv(p)
    return {"rows": len(df), "sum": int(df['value'].sum())}

if __name__ == "__main__":
    print(summarize())