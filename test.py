import get_instrument_data
import utils

api = get_instrument_data.OandaAPI()
print(api.fetch_instruments())