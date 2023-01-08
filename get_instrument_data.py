import requests
import pandas as pd 
import utils
import defs 
import configparser
import pathlib

# Parse configuartion file
script_path = pathlib.Path(__file__).parent.resolve()
parser = configparser.ConfigParser()
parser.read(f"{script_path}/configuration.conf")

# Store config variables

OANDA_URL = parser.get("oanda_config", "OANDA_URL")
OANDA_API_KEY = parser.get("oanda_config", "API_KEY")
OANDA_ACCOUNT_ID = parser.get("oanda_config", "ACCOUNT_ID")

def fetch_instruments():
    '''
    '''
    session = requests.Session()
    url =  f'{OANDA_URL}/accounts/{OANDA_ACCOUNT_ID}/instruments'
    response = session.get(
        url, 
        params=None, 
        headers= {
            'Authorization': f'Bearer {OANDA_API_KEY}'
            }
        )
    
    code, data = response.status_code, response.json()
    if code == 200:
            df = pd.DataFrame.from_dict(data['instruments'])
            df1 = df[['name','type','displayName','pipLocation','marginRate']]
            df1.to_csv(utils.get_instruments_data_filename())
    else:
        print(f"Error code : {code}")

fetch_instruments()




