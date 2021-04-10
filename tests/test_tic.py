import sys
from pathlib import Path
src_path = Path.cwd() / 'src'
sys.path.append(src_path.as_posix())

from tictronome.tictronome import Tic
from tictronome.colors import Colors

# main.py

if __name__ == "__main__":
    # Initialization
    rt = Tic(color=Colors.MAGENTA)

    # starting tic
    rt.start()

    # Some long process that takes time...
    from time import sleep
    sleep(5)

    # The End
    rt.stop()
