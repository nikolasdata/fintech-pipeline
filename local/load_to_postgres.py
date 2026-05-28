import csv
import psycopg2

import os
from dotenv import load_dotenv
load_dotenv()

password = os.environ.get("POSTGRES_PASSWORD")

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="fintech",
    user="postgres",
    password=password
)

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS eur_usd (
        date TEXT PRIMARY KEY,
        open REAL,
        high REAL,
        low REAL,
        close REAL,
        daily_range REAL
    )
""")

with open("eur_usd_transformed.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("""
            INSERT INTO eur_usd (date, open, high, low, close, daily_range)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (date) DO NOTHING
        """, (row["date"], row["open"], row["high"], row["low"], row["close"], row["daily_range"]))

conn.commit()
cursor.close()
conn.close()

print("Done! Data loaded into PostgreSQL.")