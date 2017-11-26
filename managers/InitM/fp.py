'''
Factory Pattern
'''

from entities.entities.cmc import cmcMiner
from entities.entities.cmc.cmcp import cmcParser
from entities.entities.ccap import ccapMiner
from entities.entities.ccap.ccapp import ccapParser
from entities.entities.wci import wciMiner
from entities.entities.wci.wcip import wciParser

class FactoryPattern(object):
    '''Factory Pattern'''

    def __init__(self, prName, prEntity):
        self.name = prName
        self.entity = prEntity
        self.miner = None
        self.parser = None
        self.init_entity()

    def init_entity(self):
        self.init_parser()
        self.init_miner()

    def init_miner(self):
        if str.lower(str(self.entity)) == 'cmc':
            self.miner = cmcMiner(self.name, input('API string: '), self.parser)
        if str.lower(str(self.entity)) == 'ccap':
            self.miner = ccapMiner(self.name, input('API string: '), self.parser)
        if str.lower(str(self.entity)) == 'wci':
            self.miner = wciMiner(self.name, input('API string: '), self.parser)

    def init_parser(self):
        if str.lower(str(self.entity)) == 'cmc':
            self.parser = cmcParser(self.name)
        if str.lower(str(self.entity)) == 'ccap':
            self.parser = ccapParser(self.name)
        if str.lower(str(self.entity)) == 'wci':
            self.parser = wciParser(self.name)
