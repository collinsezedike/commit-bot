import sys

from commiter import Commiter
from watcher import Watcher


def main():
    try:
        path = sys.argv[1]
        commiter = Commiter(path)
        watcher = Watcher(path)
        watcher.watch(commiter.commit)

    except IndexError:
        sys.exit(f"NullError: Please provide the path to directory you want to watch")

if __name__ == "__main__":
    main()