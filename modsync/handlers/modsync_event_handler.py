from watchdog.events import FileSystemEventHandler
import shutil


class ModsyncEventHandler(FileSystemEventHandler):
    _target = []

    def __init__(self, observer, target):
        self.observer = observer
        self._target = target

    def on_moved(self, event):
        print('moved')
        # super(LoggingEventHandler, self).on_moved(event)
        #
        # what = 'directory' if event.is_directory else 'file'
        # logging.info("Moved %s: from %s to %s", what, event.src_path,
        #              event.dest_path)

    def on_created(self, event):
        if hasattr(event, 'src_path'):
            if self._target:
                for destination in self._target:
                    try:
                        shutil.copy2(event.src_path, destination)
                    except IOError as e:
                        print(
                            'Could not copy {0} to {1} during item create in {2}. Error message: {3}'
                            .format(
                                event.src_path,
                                destination,
                                self.__class__,
                                str(e)
                            )
                        )

    def on_deleted(self, event):
        print('del')
        # super(LoggingEventHandler, self).on_deleted(event)
        #
        # what = 'directory' if event.is_directory else 'file'
        # logging.info("Deleted %s: %s", what, event.src_path)

    def on_modified(self, event):
        print('modif')
        # super(LoggingEventHandler, self).on_modified(event)
        #
        # what = 'directory' if event.is_directory else 'file'
        # logging.info("Modified %s: %s", what, event.src_path)

