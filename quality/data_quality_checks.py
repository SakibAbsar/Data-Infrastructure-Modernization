
import pandas as pd

def check_completeness(df):
    missing_values = df.isnull().sum()
    print(f"Missing values: {missing_values}")

def check_duplicates(df):
    duplicate_rows = df[df.duplicated()]
    print(f"Duplicate rows: {duplicate_rows.shape[0]}")

if __name__ == "__main__":
    df = pd.read_csv("data/processed/cleaned_data.csv")
    check_completeness(df)
    check_duplicates(df)
