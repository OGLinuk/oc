'''
Init Manager

Logic around instantiating new miner(s) to be executed
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
        return FactoryPattern(self.name, self.entity).miner
