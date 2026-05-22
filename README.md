# Fintech ELT Pipeline — EUR/USD

A simple end-to-end ELT pipeline built with Python and SQLite, pulling live forex data from the Alpha Vantage API.

## What it does

1. **Extract** — pulls daily EUR/USD exchange rate data from Alpha Vantage API
2. **Transform** — converts data types and calculates daily price range
3. **Load** — stores the transformed data into a local SQLite database

## Tech stack

- Python
- SQLite
- Alpha Vantage API
- Git

## How to run

1. Clone the repo
2. Install dependencies: `pip install requests`
3. Add your Alpha Vantage API key to `extract.py`
4. Run in order:
   - `python extract.py`
   - `python transform.py`
   - `python load.py`

## Project structure
