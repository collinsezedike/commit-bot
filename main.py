import os
import sys

from commiter import Commiter
from watcher import Watcher

def get_paths_from_gitignore():
    if os.path.isfile(".gitignore"):
        with open(".gitignore") as file:
            paths = file.readlines()
            ignore_paths = [path for path in paths if not path.startswith("#") and path.strip() != ""]
            ignore_paths = [path.strip().replace("*", "") for path in ignore_paths]
            ignore_paths.append(".git/")
            for invalid_path in ignore_paths:
                print(".git" in invalid_path)
            return ignore_paths
    return []


def main():
    try:
        path = sys.argv[1]
        commiter = Commiter(path)
        watcher = Watcher(path, paths_to_ignore=get_paths_from_gitignore())
        watcher.watch(commiter.commit)
    except IndexError:
        sys.exit(f"NullError: Please provide the path to directory you want to watch")
    except Exception as error:
        sys.exit(error)    


if __name__ == "__main__":
    main()