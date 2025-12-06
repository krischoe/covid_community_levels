"""Small Streamlit demo that shows sample data."""
import streamlit as st
import pandas as pd
from pathlib import Path

st.title("Health Data Pipeline — Demo Dashboard")

data_path = Path(__file__).resolve().parent.parent / "data" / "sample.csv"
if data_path.exists():
    df = pd.read_csv(data_path)
    st.table(df)
else:
    st.info("No sample data found. Run `python etl/ingest.py` to create sample data.")