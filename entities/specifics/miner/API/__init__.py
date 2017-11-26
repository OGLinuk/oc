'''
Generic API Miner
'''

import os
import time
import json
import requests
from entities.generics.gm import GenericMiner

class APIMiner(GenericMiner):
    '''API Miner'''

    def __init__(self, prName, prMinerAPIString, prParser):
        self.scheduledExeTime = self.set_executionTime()
        self.minerName = prName
        self.minerAPIString = prMinerAPIString
        self.rawFilePath = '/data/raw/{}RawData.json'.format(self.minerName)
        self.parser = prParser

    def set_executionTime(self):
        exeT = time.time() + 10
        return exeT

    # Execute API method
    def exe_apiCall(self):
        data = requests.get('{}'.format(self.minerAPIString)) # % (apikey)) # - uncomment if an apikey is required
        return data.json()

    # Start miner
    def run(self):
        while True:
            # Can remove line 36, only there for debugging purposes
            print('[{}miner] WAITING {} [{}miner]'.format(str.upper(self.minerName), time.time(), str.upper(self.minerName)))
            if time.time() >= self.scheduledExeTime:
                with open(self.rawFilePath, 'a+') as f:
                    json.dump(self.exe_apiCall(), f)
                print('[{}miner] FINISHED RAW DATA COLLECTION [{}miner]'.format(str.upper(self.minerName), str.upper(self.minerName)))
                time.sleep(1)
                print('[{}JP] BEGINNING PARSING STAGE [{}JP]'.format(str.upper(self.minerName), str.upper(self.minerName)))
                time.sleep(1)
                # Replaced in fp.py during init_parser()
                #self.parser = self.parser(self.minerName.split('M')[0])
                self.parser.parse()
                print('[{}JP] FINISHED PARSING STAGE [{}JP]'.format(str.upper(self.minerName), str.upper(self.minerName)))
                time.sleep(1)
                os.remove(self.rawFilePath)
            if time.time() > self.scheduledExeTime:
                break
