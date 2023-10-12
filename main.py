import os
import sys
import requests
from datetime import datetime

GITIGNORE_URL = "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"


def main():
    change_dir(".")
    write_gitignore()
    do_git_stuff()


def do_git_stuff():
    if not os.path.isdir(".git"):
        os.system("git init")
    os.system("git add .")
    os.system(f'git commit -m "auto commit on {datetime.now().date()} at {datetime.now().time()}"')


def write_gitignore():
    if not os.path.isfile(".gitignore"):
        os.system("touch .gitignore")
        with open(".gitignore", "w") as file:
            file.write(get_gitignore()) 


def change_dir(path):
    try:
        os.chdir(path)
    except FileNotFoundError:
        sys.exit(f"PathError: The system cannot find the specified psth: '{path}'")
    except Exception as error:
        sys.exit(error)


def get_gitignore():
    try:
        return requests.get(GITIGNORE_URL).text
    except requests.ConnectionError:
        sys.exit("ConnectionError: Please check your internet connection")
    except Exception as error:
        sys.exit(error)


if __name__ == "__main__":
    main()
