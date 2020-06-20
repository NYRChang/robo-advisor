# app/robo_advisor.py

import requests
import json

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
for date in dates:
    high_price = float(tsd[date]["2. high"])
    high_prices.append(high_price)

#maximum of all the high prices
recent_high = max(high_prices)


print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print(f"LATEST DAY: {latest_day}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")