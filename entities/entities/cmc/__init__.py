'''
CoinMarketCap.com miner

https://coinmarketcap.com/api/
    - https://api.coinmarketcap.com/v1/ticker/
    - https://api.coinmarketcap.com/v1/ticker/bitcoin/
    - https://api.coinmarketcap.com/v1/global/
    - https://api.coinmarketcap.com/v1/ticker/?start=100&limit=10

'''

import time
import json
import requests
from entities.specifics.miner.API import APIMiner

class cmcMiner(APIMiner):
    '''CoinMarketCap Miner'''
