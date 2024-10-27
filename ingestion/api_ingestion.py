
import requests
import pandas as pd
import os
import yaml

RAW_DATA_DIR = "./data/raw/"

def load_config():
    with open("config/config.yaml", "r") as f:
        return yaml.safe_load(f)

def ingest_api():
    config = load_config()
    response = requests.get(config["api"]["url"], headers={"Authorization": f"Bearer {config['api']['key']}" })
    if response.status_code == 200:
        data = pd.DataFrame(response.json())
        data.to_csv(os.path.join(RAW_DATA_DIR, "api_data.csv"), index=False)
        print("API data ingested successfully.")
    else:
        print(f"Failed to retrieve data: {response.status_code}")

if __name__ == "__main__":
    ingest_api()
