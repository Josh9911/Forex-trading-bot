import requests
import pandas as pd
import defs 
 
session = requests.Session()

instrument  = "EUR_USD"
count = 10
granularity = "H1"

url = f"{defs.OANDA_URL}/instruments/{instrument}/candles"


params = dict(
    count = count,
    granularity = granularity,
    price ="MBA"
)


response = session.get(url,params=params, headers = defs.SECURE_HEADER)
data = response.json()

prices = ['mid', 'bid' ,'ask']
ohlc = ['o', 'h', 'l', 'c']

our_data = []

for candle in data['candles']:
    if candle['complete'] == False:
        continue
    new_dict = {}
    new_dict ['time'] = candle['time']
    new_dict['volume'] = candle['volume']
    our_data.append(new_dict)
    for price in prices:
        for oh in ohlc:
            new_dict[f"{price}_{oh}"] = candle[price][oh]
    our_data.append(new_dict)

candles_df = pd.DataFrame.from_dict(our_data)

print(candles_df)

candles_df.to_csv("EUR_USD_H1.csv")



