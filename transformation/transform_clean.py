
import pandas as pd

PROCESSED_DATA_DIR = "./data/processed/"

def clean_data(input_file):
    df = pd.read_csv(input_file)
    df.dropna(inplace=True)
    df.to_csv(f"{PROCESSED_DATA_DIR}/cleaned_data.csv", index=False)
    print("Data cleaned and saved.")

if __name__ == "__main__":
    clean_data("data/raw/ingested_data.csv")
