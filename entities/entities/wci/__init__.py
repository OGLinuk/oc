'''
Worldcoinindex.com miner

https://www.worldcoinindex.com/apiservice
    - https://www.worldcoinindex.com/apiservice/json?key=
'''

import time
import json
import requests
from entities.entities.wci.apikey import key
from entities.specifics.miner.API import APIMiner

class wciMiner(APIMiner):
    '''Worldcoinindex.com Miner'''

    def exe_apiCall(self):
        data = requests.get('{}'.format(self.minerAPIString, key))
        return data.json()
