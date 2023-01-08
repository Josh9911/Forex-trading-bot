# Utility file to ensure that the names of the folders can be dynamically changed and will not affect the code
import pathlib
import configparser

def get_candle_data_filename(pair, granularity):
    '''
    This gets the name of the files for the candle data 
    '''
    return f"candle_data/{pair}_{granularity}.csv"

def get_instruments_data_filename():
    '''
    This gets the 
    '''
    return "instruments.csv"

def currency_names():
    our_curr = ['EUR','USD','GBP','JPY','CHF']
    return our_curr

# Parse configuartion file
script_path = pathlib.Path(__file__).parent.resolve()
parser = configparser.ConfigParser()
parser.read(f"{script_path}/configuration.conf")

# Store config variables

OANDA_URL = parser.get("oanda_config", "OANDA_URL")
OANDA_API_KEY = parser.get("oanda_config", "API_KEY")
OANDA_ACCOUNT_ID = parser.get("oanda_config", "ACCOUNT_ID")
