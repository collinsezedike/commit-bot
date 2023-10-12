import sys
import time
import logging
import pathlib

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

LOG_FILE = "watches.log"
LOG_FORMAT ="%(asctime)s - %(message)s"


class Watcher(FileSystemEventHandler):

    def __init__(self, path_to_watch, paths_to_ignore=[]):
        super().__init__()
        self.path_to_watch = path_to_watch
        self.paths_to_ignore = paths_to_ignore
        self.__logger = logging.Logger("watch_logger", level=logging.INFO)
        self.__observer = Observer()
    
    def on_any_event(self, event):
        if event.event_type not in ["opened", "closed"] \
            and self.__is_valid_watch_path(event.src_path):
            self.__log(event)
            self.__special_func()
    
    def __is_valid_watch_path(self, path_that_changed):
        for invalid_path in self.paths_to_ignore:
            if invalid_path in path_that_changed:
                return False
        return True
    
    def __log(self, event):
        what = "directory" if event.is_directory else "file"
        log_message = f"{event.event_type} {what} {event.src_path}"
        self.__logger.info(log_message)
    
    def watch(self, func):
        self.__special_func = func  # call when the watcher detects a change
        self.__observer.schedule(self, self.path_to_watch, recursive=True)
        self.__observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.__observer.stop()
        except Exception as error:
            print(error)
        finally:
            self.__observer.join()
            sys.exit()
