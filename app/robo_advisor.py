# app/robo_advisor.py

import json
import csv
import os

import requests

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo"
response = requests.get(request_url)
#print(type(response))    #<class 'requests.models.Response'>
#print(response.status_code)         #200
#print(response.text)        #STRING

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

parsed_response = json.loads(response.text)
tsd = parsed_response["Time Series (Daily)"]

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

dates = list(tsd.keys())    #TODO: assumes first day is on top but consider sorting to ensure 1st day is on top
latest_day = dates[0]
latest_close = tsd[latest_day]["4. close"]

#get high price of each day
high_prices = []
low_prices = []
for date in dates:
    high_price = float(tsd[date]["2. high"])
    high_prices.append(high_price)
    low_price = float(tsd[date]["3. low"])
    low_prices.append(low_price)

#max/min of all the high prices
recent_high = max(high_prices)
recent_low = min(low_prices)

csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")
csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

with open(csv_file_path, "w", newline='') as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above
    
    #looping
    writer.writerow({
        "timestamp": "To-do",
        "open": "To-do",
        "high": "To-do",
        "low": "To-do",
        "close": "To-do",
        "volume": "To-do"
        })
    writer.writerow({
        "timestamp": "To-do",
        "open": "To-do",
        "high": "To-do",
        "low": "To-do",
        "close": "To-do",
        "volume": "To-do"
        })
    


print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print(f"LATEST DAY: {latest_day}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print(f"WRITING DATA TO CSV: {csv_file_path}")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")



