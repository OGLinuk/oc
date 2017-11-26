'''
JSON Parser
'''

import os
import json
import time
from entities.generics.gp import GenericParser

class JSONParser(GenericParser):
    '''JSON Parser'''

    # Loads and returns the raw JSON data produced by the miner(s)
    def get_rawData(self):
        with open(self.rawFilePath) as f:
            data = json.loads(f.read())
        return data
