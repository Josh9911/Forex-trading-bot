import requests
import pandas as pd
import utils

def fetch_candles(instrument, count, granularity):
    session = requests.Session()

    url = f"{utils.OANDA_URL}/instruments/{instrument}/candles"
    
    params = dict(
        count = count,
        granularity = granularity,
        price = "MBA"
    )
    response = session.get(
        url,
        params=params,
        headers= {
            'Authorization': f'Bearer {utils.OANDA_API_KEY}'
            }
        )

    code, data = response.status_code, response.json()

    if code !=200:
        print(f"{instrument}Error")
    else:
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

        print(f"{instrument} loaded {candles_df.shape[0]} candles from {candles_df.time.min()} to {candles_df.time.max()}")
        candles_df.to_csv(f"candle_data/{instrument}_{granularity}.csv")

currency_pair_list = utils.currency_names()
ins_df = pd.read_csv("instruments.csv")

for p1 in currency_pair_list:
    for p2 in currency_pair_list:
        currency_pair = f"{p1}_{p2}"
        if currency_pair in ins_df.name.unique():
            fetch_candles(currency_pair,100,"H1")