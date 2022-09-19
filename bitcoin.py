import urllib.request
import json

data = urllib.request.urlopen("http://api.bitcoincharts.com/v1/weighted_prices.json")

def convert_to_bitcoin(amount, currency):
    bitcoins = json.loads(data.read())
    converted = float(bitcoins[currency]["24h"]) * amount
    print(converted)


convert_to_bitcoin(1, "USD")