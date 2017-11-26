'''
CoinCap.io Parser
'''

import json
import time
from entities.specifics.parser.JSON import JSONParser

class ccapParser(JSONParser):
    '''CoinCap.io JSON Parser'''

    def parse(self):
        jsonData = self.get_rawData()

        for currency in jsonData[0:]:
            with open(self.parsedFilePath, 'ab+') as f:
                f.write(bytes('{}/{}/{}/{}\n'.format(time.asctime(time.localtime(time.time())), currency['long'], currency['price'], currency['perc']), 'UTF-8'))

        print('[CCAPJP] JSON DATA PARSED [CCAPJP]')
