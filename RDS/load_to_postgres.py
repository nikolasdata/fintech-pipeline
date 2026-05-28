import csv
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    host=os.environ.get("RDS_HOST"),
    port=5432,
    database="fintech",
    user="postgres",
    password=os.environ.get("RDS_PASSWORD"),
    sslmode="require"
)

cursor = conn.cursor()

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
print("Done! Data loaded into RDS PostgreSQL.")