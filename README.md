# Fintech ELT Pipeline — EUR/USD

An end-to-end ELT pipeline built with Python, PostgreSQL, and dbt, pulling live forex data from the Alpha Vantage API and modelling it for financial analysis.

## What it does

1. **Extract** — pulls daily EUR/USD exchange rate data from Alpha Vantage API
2. **Transform** — converts data types and calculates daily price range
3. **Load** — stores transformed data into a PostgreSQL database
4. **Upload** — pushes raw and transformed data to AWS S3
5. **Model** — runs dbt models for analytical reporting

## Tech stack

- Python
- PostgreSQL
- dbt Core
- AWS S3
- Alpha Vantage API
- Git

## How to run

1. Clone the repo
2. Install dependencies: `pip install requests python-dotenv psycopg2-binary boto3 dbt-core dbt-postgres`
3. Create a `.env` file with your credentials:
4. Run the pipeline:
   python run_pipeline.py
5. Run dbt models:
   cd forex_models
   dbt run
## dbt models

| Model | Description |
|---|---|
| `daily_volatility` | Top 10 most volatile EUR/USD trading days |
| `monthly_summary` | Average, high, and low close price per month |
| `trend_detection` | 30-day rolling average of close price |

## Project structure

    fintech-pipeline/
    ├── extract.py              # pulls data from Alpha Vantage API
    ├── transform.py            # cleans and adds daily_range column
    ├── load.py                 # loads into SQLite (local backup)
    ├── load_to_postgres.py     # loads into PostgreSQL
    ├── upload_to_s3.py         # uploads CSVs to AWS S3
    ├── run_pipeline.py         # runs full pipeline in sequence
    ├── forex_models/           # dbt project
    │   └── models/
    │       ├── daily_volatility.sql
    │       ├── monthly_summary.sql
    │       └── trend_detection.sql
    └── .env                    # credentials (not committed to GitHub)
## Security

Credentials are stored in a `.env` file and excluded from version control via `.gitignore`.
