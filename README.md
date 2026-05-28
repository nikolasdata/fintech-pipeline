Here's the updated README:
markdown# Fintech ELT Pipeline — EUR/USD

An end-to-end ELT pipeline built with Python, PostgreSQL, dbt, and AWS, pulling live forex data from the Alpha Vantage API and modelling it for financial analysis.

## What it does

1. **Extract** — pulls daily EUR/USD exchange rate data from Alpha Vantage API
2. **Transform** — converts data types and calculates daily price range
3. **Load** — stores transformed data into PostgreSQL (local and AWS RDS)
4. **Upload** — pushes raw data to AWS S3
5. **Model** — runs dbt analytical models on top of the data
6. **Automate** — AWS Lambda and EventBridge run the pipeline daily in the cloud

## Tech stack

- Python
- PostgreSQL (local) / AWS RDS (cloud)
- dbt Core
- AWS S3, Lambda, EventBridge
- Alpha Vantage API
- Git

## Architecture
EventBridge (daily schedule)
→ Lambda: extract.py → S3 (raw data)
→ Lambda: transform.py → RDS PostgreSQL
→ dbt models → analytical views

## How to run locally

1. Clone the repo
2. Install dependencies:
pip install requests python-dotenv psycopg2-binary boto3 dbt-core dbt-postgres
3. Create a `.env` file:
ALPHA_VANTAGE_KEY=your_key
POSTGRES_PASSWORD=your_password
RDS_HOST=your_rds_endpoint
RDS_PASSWORD=your_rds_password
4. Run the local pipeline:
python local/run_pipeline.py
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
├── local/                  # local pipeline scripts
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── load_to_postgres.py
│   ├── upload_to_s3.py
│   └── run_pipeline.py
├── lambda/                 # AWS Lambda functions
│   ├── extract.py
│   └── transform.py
├── RDS/                    # RDS connection scripts
│   └── load_to_postgres.py
├── forex_models/           # dbt project
│   └── models/
│       ├── daily_volatility.sql
│       ├── monthly_summary.sql
│       └── trend_detection.sql
├── .gitignore
└── README.md

## Security

Credentials are stored in a `.env` file and excluded from version control via `.gitignore`.