# forex_models — dbt Project

dbt models for the Fintech ELT Pipeline, running analytical transformations on EUR/USD forex data stored in PostgreSQL.

## Models

| Model | Description |
|---|---|
| `daily_volatility` | Top 10 most volatile EUR/USD trading days ranked by daily price range |
| `monthly_summary` | Average, high, and low close price per month |
| `trend_detection` | 30-day rolling average of close price using SQL window functions |

## How to run

    dbt run                                    # build all models
    dbt test                                   # run data tests


## Connection

Connects to PostgreSQL (local or AWS RDS). Configure credentials in `~/.dbt/profiles.yml`.