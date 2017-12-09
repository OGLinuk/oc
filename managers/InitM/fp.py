'''
Factory Pattern

Logic around actual instantiation of entities
'''

from entities.entities.cmc import cmcMiner
from entities.entities.cmc.cmcp import cmcParser
from entities.entities.ccap import ccapMiner
from entities.entities.ccap.ccapp import ccapParser
from entities.entities.wci import wciMiner
from entities.entities.wci.wcip import wciParser
# Add path to new entity

class FactoryPattern(object):
    '''Factory Pattern'''

    def __init__(self, prName, prEntity):
        self.name = prName
        self.entity = prEntity
        self.parser = self.init_parser()
        self.miner = self.init_miner()

    # Instantiate miner
    def init_miner(self):
        miner = None
        if str.lower(str(self.entity)) == 'cmc':
            miner = cmcMiner(self.name, input('API string: '), self.parser)
        if str.lower(str(self.entity)) == 'ccap':
            miner = ccapMiner(self.name, input('API string: '), self.parser)
        if str.lower(str(self.entity)) == 'wci':
            miner = wciMiner(self.name, input('API string: '), self.parser)
        # if str.lower(str(self.entity)) == 'new entity':
        #   miner = newMiner(*args, **kwargs)
        return miner

    # Instantiate parser
    def init_parser(self):
        parser = None
        if str.lower(str(self.entity)) == 'cmc':
            parser = cmcParser(self.name)
        if str.lower(str(self.entity)) == 'ccap':
            parser = ccapParser(self.name)
        if str.lower(str(self.entity)) == 'wci':
            parser = wciParser(self.name)
        # if str.lower(str(self.entity)) == 'new entity':
        #   parser = newParser(*args, **kwargs)
        return parser
