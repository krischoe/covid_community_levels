import requests, csv, io, os
# from google.cloud import storage  # if using GCP

DATA_URL = "https://data.cdc.gov/api/views/3nnm-4jni/rows.csv" 

def download_csv(url, out_path="data/raw.csv"):
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    with open(out_path, "wb") as f:
        f.write(r.content)
    print("Saved:", out_path)

if __name__ == "__main__":
    download_csv(DATA_URL)
