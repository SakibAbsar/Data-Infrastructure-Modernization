# Data-Infrastructure-Modernization
## Overview
This project demonstrates an end-to-end data engineering solution that supports data ingestion, transformation, quality control, real-time processing, and warehousing.

## Architecture
![Pipeline Architecture](docs/architecture_diagram.png)

## Setup and Configuration
1. Install dependencies: `pip install -r requirements.txt`
2. Configure `config/config.yaml` and `config/credentials.json` with your API keys, database details, etc.

## Running the Pipeline
1. Run batch ingestion: `python ingestion/batch_ingestion.py`
2. Transform data: `python transformation/transform_clean.py`
3. Load data to warehouse: `python warehousing/load_to_warehouse.py`

See `docs/pipeline_steps.md` for more detailed instructions.
