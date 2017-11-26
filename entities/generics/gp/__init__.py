'''
Generic Parser
'''

import os
import abc
import time

class GenericParser(object):
    '''Generic Parser'''

    def __init__(self, prName):
        self.parserName = '{}p'.format(prName)
        self.rawFilePath = 'data/raw/{}RawData.json'.format(prName)
        self.parsedFilePath = 'data/parsed/{}ParsedData.txt'.format(prName)

    # Loads and returns the raw data produced by the miner(s)
    @abc.abstractmethod
    def get_rawData(self):
        raise NotImplementedError()

    # Parse method that extracts specific information.
    @abc.abstractmethod
    def parse(self):
        raise NotImplementedError()
