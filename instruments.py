import requests
import pandas as pd 
import utils
import old_files.defs as defs 
 

class Instrument():
    def __init__(self,ob):
        self.name = ob['name']
        self.ins_type = ob['type']
        self.displayName = ob['displayName']
        self.pipLocation = pow(10, ob['pipLocation']) 
        self.marginRate = ob['marginRate']
    
    def __repr__(self):
        return str(vars(self))
    
    @classmethod
    def get_instruments_df(cls):
        '''
        Get the df of the Dataframe of all the instruments
        '''
        return pd.read_csv(utils.get_instruments_data_filename())

    @classmethod
    def get_instruments_list(cls):
        '''
        Create an Instrument Object for all the instruments avaliable
        '''
        df = cls.get_instruments_df()
        return [Instrument(x) for x in df.to_dict(orient = 'records')]

    @classmethod
    def get_instrument_dict(cls):
        i_list = cls.get_instruments_list()
        i_keys = [x.name for x in i_list]
        return { k:v for (k,v) in zip(i_keys, i_list) }  

    @classmethod
    def get_instrument_by_name(cls,pairname):
        d = cls.get_instrument_dict()
        if pairname in d:
            return d[pairname]
        else:
            return None

if __name__ == "__main__":
    print(Instrument.get_instrument_dict())

