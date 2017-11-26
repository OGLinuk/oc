'''
CoinMarketCap.com miner

https://coinmarketcap.com/api/
    - https://api.coinmarketcap.com/v1/ticker/
'''

import time
import json
import requests
from entities.specifics.miner.API import APIMiner

class cmcMiner(APIMiner):
    '''CoinMarketCap Miner'''
