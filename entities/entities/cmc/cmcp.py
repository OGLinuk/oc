'''
CoinMarketCap Parser
'''

import json
import time
from entities.specifics.parser.JSON import JSONParser

class cmcParser(JSONParser):
    '''CoinMarketCap Parser'''

    def parse(self):
        jsonData = self.get_rawData()

        for currency in jsonData[0:]:
            with open(self.parsedFilePath, 'ab+') as f:
                f.write(bytes('{}/{}/{}/{}/{}/{}\n'.format(time.asctime(time.localtime(time.time())), currency['name'], currency['price_usd'], currency['percent_change_1h'], currency['percent_change_24h'], currency['percent_change_7d']), 'UTF-8'))

        print('[CMCJP] JSON DATA PARSED [CMCJP]')
