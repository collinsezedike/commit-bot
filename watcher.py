import time
import logging
import pathlib

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

LOG_FILE = "changes.log"

class Watcher(FileSystemEventHandler):

    def __init__(self, path_to_watch):
        super().__init__()
        self.__path = path_to_watch
        self.__observer = Observer()
        logging.basicConfig(filename=LOG_FILE,
                    level=logging.INFO,
                    format="%(asctime)s - %(message)s", 
                    datefmt="%Y-%m-%d %H:%M:%S")
    
    def on_any_event(self, event):
        if event.event_type not in ["opened", "closed"] \
            and pathlib.Path(event.src_path).suffix != ".log":
            self.__log(event)
            self.__special_func()
        return super().on_any_event(event)
    
    def __log(self, event):
        what = "directory" if event.is_directory else "file"
        log_message = f"{event.event_type} {what} {event.src_path}"
        logging.info(log_message)
    
    def watch(self, func):
        self.__special_func = func  # special function defines what should happen when the watched detects a change
        self.__observer.schedule(self, self.__path, recursive=True)
        self.__observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.__observer.stop()
        self.__observer.join()