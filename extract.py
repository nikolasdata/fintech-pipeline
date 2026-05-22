import requests
import csv

API_KEY = "818XF7I47058AD92"  # paste your Alpha Vantage key here
symbol = "EUR/USD"

url = f"https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=EUR&to_symbol=USD&apikey={API_KEY}"

response = requests.get(url)
data = response.json()


rates = data["Time Series FX (Daily)"]

with open("eur_usd_raw.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["date", "open", "high", "low", "close"])
    for date, values in rates.items():
        writer.writerow([
            date,
            values["1. open"],
            values["2. high"],
            values["3. low"],
            values["4. close"]
        ])

print("Done! File saved as eur_usd_raw.csv")