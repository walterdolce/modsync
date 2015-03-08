import distutils
from watchdog.events import FileSystemEventHandler
import shutil
import os
import errno
import distutils.dir_util


class ModsyncEventHandler(FileSystemEventHandler):
    _target = []
    _source = ''

    def __init__(self, observer, source, target):
        self.observer = observer
        self._source = source
        self._target = target

    def on_moved(self, event):
        print('moved')

    def on_created(self, event):
        if hasattr(event, 'src_path') and self._target:
            for destination in self._target:
                try:
                    if os.path.isdir(event.src_path):
                        try:
                            files = os.listdir(event.src_path)
                            if not files:
                                os.mkdir(destination + os.sep + event.src_path.replace(self._source, ''))
                        except NotImplementedError:
                            raise Exception('os.listdir has thrown a NotImplementedError on the current OS')
                    else:
                        shutil.copy2(event.src_path, destination)
                except Exception as e:
                        print(
                            'Could not copy "{0}" to "{1}" during item create in "{2}".{3} Error message: {4}'
                            .format(
                                event.src_path,
                                destination,
                                self.__class__,
                                os.linesep,
                                str(e)
                            )
                        )

    def on_deleted(self, event):
        print('del')

    def on_modified(self, event):
        print('modif')