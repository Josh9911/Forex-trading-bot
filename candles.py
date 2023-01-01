import requests 
import defs 
import pandas as pd

session = requests.Session()

ins_df = pd.read_pickle("instruments.pkl")

def fetch_candles(pair_name, count, granularity):
    url = f"{defs.OANDA_URL}/instruments/{pair_name}/candles"
    
    params = dict(
        count = count,
        granularity = granularity,
        price = "MBA"
    )
    response = session.get(url, params=params, headers = defs.SECURE_HEADER)

    return response.status_code, response.json()

def get_candles_df(json_response):

    our_data = []

    prices = ['mid', 'bid' ,'ask']
    ohlc = ['o', 'h', 'l', 'c']

    for candle in json_response['candles']:
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

    return candles_df

def save_file(candles_df, pair, granularity):
    candles_df.to_pickle(f"candle_data/{pair}_{granularity}.pkl")

def create_data(pair,granularity):
    code, json_data = fetch_candles(pair, 100, granularity)
    if code != 200:
        print(pair, "Error")
        return
    df = get_candles_df(json_data)
    print(f"{pair} loaded {df.shape[0]} candles from {df.time.min()} to {df.time.max()}")
    
    save_file(df, pair, granularity)


our_curr = ['EUR','USD','GBP','JPY','CHF','NZD','CAD']

for p1 in our_curr:
    for p2 in our_curr:
        pair = f"{p1}_{p2}"
        if pair in ins_df.name.unique():
            create_data(pair,"H1")
