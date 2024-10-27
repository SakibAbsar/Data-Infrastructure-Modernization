
import pandas as pd
import os

RAW_DATA_DIR = "./data/raw/"

def ingest_csv(file_path):
    try:
        data = pd.read_csv(file_path)
        data.to_csv(os.path.join(RAW_DATA_DIR, "ingested_data.csv"), index=False)
        print("Batch data ingested successfully.")
    except Exception as e:
        print(f"Error during batch ingestion: {e}")

if __name__ == "__main__":
    ingest_csv("path/to/your/file.csv")
