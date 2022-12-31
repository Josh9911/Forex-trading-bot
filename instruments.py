import requests
import pandas as pd 

import defs 
 
session = requests.Session()

instrument  = "EUR_USD"
count = 10
granularity = "H1"

url = f"{defs.OANDA_URL}/accounts/{defs.ACCOUNT_ID}/instruments"



response = session.get(url,params=None, headers = defs.SECURE_HEADER)

data = response.json()

instruments = data['instruments']

instrument_data = []
for item in instruments:
    new_ob = dict(
    name = item['name'],
    type = item['type'],
    displayName = item['displayName'],
    pipLocation = item['pipLocation'],
    marginRate = item['marginRate']
    )
    instrument_data.append(new_ob)

instrument_df = pd.DataFrame.from_dict(instrument_data)

print(instrument_df)

instrument_df.to_pickle("instruments.pkl")
