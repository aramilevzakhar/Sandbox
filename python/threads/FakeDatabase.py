import logging
import time
import threading
import os



class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()
    def update(self, name):
        logging.info("Thread %s: starting update", name)
        logging.debug("Thread %s about to lock", name)

        # Этот ._lock инициализируется в разблокированном состоянии, блокируется и освобождается оператором with.
        with self._lock:
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy



        logging.debug("Thread %s after release", name)
        logging.info("Thread %s: finishing update", name)


#
#class FakeDatabase:
#    def __init__(self):
#        self.value = 0
#        self._lock = threading.Lock()
#    def locked_update(self, name):
#        logging.info("Thread %s: starting update", name)
#        logging.debug("Thread %s about to lock", name)
#        with self._lock:
#            logging.debug("Thread %s has lock", name)
#            local_copy = self.value
#            local_copy += 1
#            time.sleep(0.1)
#            self.value = local_copy
#            logging.debug("Thread %s about to release lock", name)
#        logging.debug("Thread %s after release", name)
#        logging.info("Thread %s: finishing update", name)
