'''
Worldcoinindex.com Parser
'''

import json
import time
from entities.specifics.parser.JSON import JSONParser

class wciParser(JSONParser):
    '''Worldcoinindex.com JSON Parser'''

    def parse(self):
        jsonData = self.get_rawData()

        for currency in jsonData["Markets"][0:]:
            with open('data/parsed/wciParsedData.txt', 'ab+') as f:
                f.write(bytes('{}/{}/{}\n'.format(time.asctime(time.localtime(time.time())), currency['Name'], currency['Price_usd']), 'UTF-8'))

        print('[WCIJP] JSON DATA PARSED [WCIP]')
