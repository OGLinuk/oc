'''
Generic Miner
'''

import abc
import time

class GenericMiner(object):
    '''Generic Miner'''
    
    def __init__(self, prName):
        self.minerName = prName
        self.scheduledExeTime = self.set_executionTime()
        self.rawFilePath = None

    # Set execution time interval
    @abc.abstractmethod
    def set_executionTime(self):
        raise NotImplementedError()
        
    # Return path to raw data
    def get_rawDataPath(self):
        return self.rawFilePath
        
    # Start miner 
    @abc.abstractmethod
    def run(self):
        raise NotImplementedError()