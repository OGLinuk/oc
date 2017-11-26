'''
Init Manager
'''

from managers.InitM.fp import FactoryPattern

class InitManager(object):
    '''Init Manager'''

    def __init__(self):
        self.name = None
        self.entity = None

    def init_Req(self):
        self.name = input('Name: ')
        self.entity = input('Entity: ')
        miner = self.init_Entity()
        return miner

    def init_Entity(self):
        return FactoryPattern(self.name, self.entity).miner
