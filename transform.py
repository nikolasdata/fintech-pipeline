import csv

with open("eur_usd_raw.csv", "r") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

transformed = []
for row in rows:
    transformed.append({
        "date": row["date"],
        "open": float(row["open"]),
        "high": float(row["high"]),
        "low": float(row["low"]),
        "close": float(row["close"]),
        "daily_range": round(float(row["high"]) - float(row["low"]), 5)
    })

with open("eur_usd_transformed.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["date", "open", "high", "low", "close", "daily_range"])
    writer.writeheader()
    writer.writerows(transformed)

print(f"Done! {len(transformed)} rows transformed.")