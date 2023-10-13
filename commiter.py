import os
import sys
import logging
import pathlib
import requests
from datetime import datetime

GITIGNORE_URL = "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"
LOG_FILE = f"{os.getcwd()}/commits.log"


class Commiter:

    def __init__(self, path):
        self.__watch_dir = pathlib.Path(path).absolute()

        self.__logger = logging.getLogger("commit_logger")
        self.__logger.setLevel(level=logging.INFO)
        format = logging.Formatter("%(message)s", datefmt="%Y-%m-%d %H:%M:%S")
        handler =   logging.FileHandler(LOG_FILE)
        handler.setFormatter(format)
        self.__logger.addHandler(handler)

        self.__write_gitignore()
        
    def __get_gitignore(self):
        try:
            return requests.get(GITIGNORE_URL).text
        except requests.ConnectionError:
            sys.exit("ConnectionError: Please check your internet connection")
        except Exception as error:
            sys.exit(error)

    def __write_gitignore(self):
        if not os.path.isfile(f"{self.__watch_dir}/.gitignore"):
            os.system(f"touch {self.__watch_dir}/.gitignore")
            with open(f"{self.__watch_dir}/.gitignore", "w") as file:
                file.write(self.__get_gitignore())

    def __log(self, message):
        self.__logger.info(message)

    def commit(self):
        commit_message = f"auto commit on {datetime.now().date()} at {datetime.now().time().strftime('%H:%M:%S')}"
        if not os.path.isdir(f".git"):
            os.system("git init")
        os.system(f"git add {self.__watch_dir}")
        os.system(f'git commit -m "{commit_message}"')
        self.__log(commit_message)
