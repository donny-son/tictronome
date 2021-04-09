import sys
from pathlib import Path

sys.path.append(Path.cwd().parent.as_posix())
sys.path.append(Path.cwd().as_posix())

from tictronome import Tic

# main.py

if __name__ == "__main__":
    # Initialization
    rt = Tic()

    # Some long process that takes time...
    from time import sleep

    sleep(5)

    # The End
    rt.stop()
