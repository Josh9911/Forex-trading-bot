import requests
from requests.exceptions import HTTPError
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
print (response.json())

