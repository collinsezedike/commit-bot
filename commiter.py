import os
import sys
import logging
import requests
from datetime import datetime
from logging import Logger

GITIGNORE_URL = "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"
LOG_FORMAT ="%(asctime)s - %(message)s"
LOG_FILE = "commits.log"
#datefmt="%Y-%m-%d %H:%M:%S")


class Commiter:

    def __init__(self, path):
        self.__path = path
        self.__logger = Logger("commit_logger", level=logging.INFO)
        self.__change_to_watch_dir()
        self.__write_gitignore()

    def __change_to_watch_dir(self):
        try:
            os.chdir(self.__path)
        except FileNotFoundError:
            sys.exit(f"PathError: The system cannot find the specified path: '{self.__path}'")
        except Exception as error:
            sys.exit(error)
        
    def __get_gitignore(self):
        try:
            return requests.get(GITIGNORE_URL).text
        except requests.ConnectionError:
            sys.exit("ConnectionError: Please check your internet connection")
        except Exception as error:
            sys.exit(error)

    def __write_gitignore(self):
        if not os.path.isfile(".gitignore"):
            os.system("touch .gitignore")
            with open(".gitignore", "w") as file:
                file.write(self.__get_gitignore()) 

    def __log(self, message):
        self.__logger = logging.getLogger("commit_logger")
        handler = self.__logger.addHandler(LOG_FILE)
        handler.setFormatter()
        self.__logger.info(message)

    def commit(self):
        commit_message = f"auto commit on {datetime.now().date()} at {datetime.now().time()}"
        if not os.path.isdir(".git"):
            os.system("git init")
        os.system("git add .")
        os.system(f'git commit -m "{commit_message}"')
        self.__log(commit_message)
