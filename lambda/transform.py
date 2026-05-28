import csv
import boto3
import psycopg2
import os
from io import StringIO

def lambda_handler(event, context):
    s3 = boto3.client("s3")
    
    obj = s3.get_object(Bucket="nikolasdata-fintech-pipeline", Key="eur_usd_raw.csv")
    content = obj["Body"].read().decode("utf-8")
    
    reader = csv.DictReader(StringIO(content))
    rows = list(reader)
    
    transformed = []
    for row in rows:
        transformed.append((
            row["date"],
            float(row["open"]),
            float(row["high"]),
            float(row["low"]),
            float(row["close"]),
            round(float(row["high"]) - float(row["low"]), 5)
        ))
    
    conn = psycopg2.connect(
        host=os.environ.get("RDS_HOST"),
        port=5432,
        database="fintech",
        user="postgres",
        password=os.environ.get("RDS_PASSWORD"),
        sslmode="require"
    )
    
    cursor = conn.cursor()
    
    for row in transformed:
        cursor.execute("""
            INSERT INTO eur_usd (date, open, high, low, close, daily_range)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (date) DO NOTHING
        """, row)
    
    conn.commit()
    cursor.close()
    conn.close()
    
    return {"statusCode": 200, "body": f"Transformed and loaded {len(transformed)} rows"}