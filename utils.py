# Utility file to ensure that the names of the folders can be dynamically changed and will not affect the code


def get_candle_data_filename(pair, granularity):
    '''
    This gets the name of the files for the candle data 
    '''
    return f"candle_data/{pair}_{granularity}.pkl"

def get_instruments_data_filename():
    '''
    This gets the 
    '''
    return "instruments.pkl"

