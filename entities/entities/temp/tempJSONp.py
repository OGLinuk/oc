'''
Template Parser
'''

import json
import time
from entities.specifics.parser.JSON import JSONParser

class templateJSONParser(JSONParser):
    '''Template JSON Parser'''

    def parse(self):
        raise NotImplementedError()
