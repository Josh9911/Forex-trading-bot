import requests
import pandas as pd
import defs
import utils

class OandaAPI():

    def __init__(self) -> None:
        self.session = requests.Session()
    
    def fetch_instruments(self):
        '''
        Makes a GET request to obtain the instruments and returns the status code and the json response
        '''
        url =  f'{defs.OANDA_URL}/accounts/{defs.ACCOUNT_ID}/instruments'
        response = self.session.get(url, params=None, headers= defs.SECURE_HEADER)
        return response.status_code, response.json()

    def get_instruments_df(self):
        '''
        Converts the instruments json response to a dataframe if the status code is not an error
        '''
        code, data = self.fetch_instruments()
        if code == 200:
            df = pd.DataFrame.from_dict(data['instruments'])
            return df[['name','type','displayName','pipLocation','marginRate']]
        else:
            return None

    def save_instruments_df(self):
        '''
        Saves the dataframe into a csv file to be used later 
        '''
        df = self.get_instruments_df()
        if df is not None:
            df.to_csv(utils.get_instruments_data_filename())


    def fetch_candles(self, pair_name, count, granularity):
        '''
        Fetches the candles and returns the status code and the data in a json format
        '''
        url = f"{defs.OANDA_URL}/instruments/{pair_name}/candles"
    
        params = dict(
            count = count,
            granularity = granularity,
            price = "MBA"
        )
        response = self.session.get(url, params=params, headers = defs.SECURE_HEADER)

        return response.status_code, response.json()

if __name__ == '__main__':
    api = OandaAPI()
    api.save_instruments_df()