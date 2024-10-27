
import pandas as pd
import psycopg2
import yaml

def load_config():
    with open("config/config.yaml", "r") as f:
        return yaml.safe_load(f)

def load_to_db(df, table_name):
    config = load_config()
    conn = psycopg2.connect(
        host=config["database"]["host"],
        port=config["database"]["port"],
        user=config["database"]["user"],
        password=config["database"]["password"],
        dbname=config["database"]["database"]
    )
    df.to_sql(table_name, conn, if_exists='append', index=False)
    conn.close()
    print(f"Data loaded to {table_name}.")

if __name__ == "__main__":
    df = pd.read_csv("data/processed/cleaned_data.csv")
    load_to_db(df, "users")
