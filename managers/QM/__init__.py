'''
Queue Manager
'''

import os
import time
import threading
from managers.InitM import InitManager

class QueueManager(object):
    '''Queue Manager'''

    def __init__(self):
        self.threads = []
        self.miners = []
        self.stage_miners()

    # Get/instantiate number of entities, then append them to the list of miners
    def exe_prep(self):
        nEntities = int(input('Number of Entities: '))
        init = InitManager()
        for i in range(0, nEntities):
            m = init.init_Req()
            self.miners.append(m)

    # Queue each miner into its own thread
    def queue_threads(self):
        for miner in self.miners:
            thread = threading.Thread(target=miner.run)
            self.threads.append(thread)

    # Execute the 2 above methods, then start() -> join() every thread
    def stage_miners(self):
        self.exe_prep()
        self.queue_threads()
        [thread.start() for thread in self.threads]
        [thread.join() for thread in self.threads]
