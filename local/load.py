import csv
import sqlite3

conn = sqlite3.connect("eur_usd.db")
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
            INSERT OR REPLACE INTO eur_usd VALUES (?, ?, ?, ?, ?, ?)
        """, (row["date"], row["open"], row["high"], row["low"], row["close"], row["daily_range"]))

conn.commit()
conn.close()

print("Done! Data loaded into eur_usd.db")