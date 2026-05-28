import requests
import csv
import os
import boto3
from io import StringIO

def lambda_handler(event, context):
    API_KEY = os.environ.get("ALPHA_VANTAGE_KEY")
    
    url = f"https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=EUR&to_symbol=USD&apikey={API_KEY}"
    
    response = requests.get(url)
    data = response.json()
    
    rates = data["Time Series FX (Daily)"]
    
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["date", "open", "high", "low", "close"])
    for date, values in rates.items():
        writer.writerow([
            date,
            values["1. open"],
            values["2. high"],
            values["3. low"],
            values["4. close"]
        ])
    
    s3 = boto3.client("s3")
    s3.put_object(
        Bucket="nikolasdata-fintech-pipeline",
        Key="eur_usd_raw.csv",
        Body=output.getvalue()
    )
    
    lambda_client = boto3.client("lambda")
    lambda_client.invoke(
        FunctionName="fintech-transform",
        InvocationType="Event"
    )
    
    return {"statusCode": 200, "body": "Extract complete"}