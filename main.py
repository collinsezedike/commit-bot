import os
import sys

from commiter import Commiter
from watcher import Watcher

def get_paths_from_gitignore():
    if not os.path.isfile(".gitignore"):
        with open(".gitignore") as file:
            paths = file.readlines()
            for path in paths:
                path.replace("*", "")
                if path.startswith("#") or path.strip() == "":
                    paths.pop(path.index)
            print(paths)
            return paths
    return []

def main():
    try:
        path = sys.argv[1]
        commiter = Commiter(path)
        watcher = Watcher(path_to_watch=path, paths_to_ignore=get_paths_from_gitignore())
        watcher.watch(commiter.commit)

    except IndexError:
        sys.exit(f"NullError: Please provide the path to directory you want to watch")

if __name__ == "__main__":
    main()