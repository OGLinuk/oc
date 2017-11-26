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

    def exe_prep(self):
        nMiners = int(input('N of Miners: '))
        init = InitManager()
        for i in range(0, nMiners):
            m = init.init_Req()
            self.miners.append(m)

    def queue_threads(self):
        for miner in self.miners:
            thread = threading.Thread(target=miner.run)
            self.threads.append(thread)

    def stage_miners(self):
        self.exe_prep()
        self.queue_threads()
        [thread.start() for thread in self.threads]
        [thread.join() for thread in self.threads]
