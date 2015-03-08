from modsync.handlers.modsync_event_handler import ModsyncEventHandler
from watchdog.observers import Observer
from modsync.handlers.modsync_event_handler import ModsyncEventHandler
import time


class Modsync:
    _target = []
    _source = ''
    _observer = None

    def __init__(self):
        pass

    def setSource(self, source):
        self._source = source

    def setTarget(self, target_dir):
        self._target.append(target_dir)

    def getObserver(self):
        return self._observer

    def run(self):

        if not self._source:
            return 0

        self._observer = Observer()
        event_handler = ModsyncEventHandler(self._observer, self._target)
        self._observer.schedule(event_handler, self._source, recursive=True)
        self._observer.start()
        try:
            time.sleep(10)
            pass
        except KeyboardInterrupt:
            self._observer.stop()
        self._observer.join()
        return 0