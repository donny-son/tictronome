import threading
from typing import Optional
from .colors import Colors, ColoredString
from time import sleep


class Tic:
    """Different thread to show if your interpreter is running.

    May or may not relieve stress when waiting for a long function to run.

    Usage:
        1. Initialize the Tic.
        2. Invokes the start method at the point where the code starts.
        2. Stop the Tic at a desired location.

    methods:
        start: Start Tic.
        stop: Stop Tic.
    
    Example:
        from tic import Tic  # import Tic class
        tic = Tic(0.1, print_seconds=False)  # initialize before a long function call
        some_long_function_to_process(...)  # the long function call
        tic.stop()  # end of script or wherever you want it to end
        
    """

    def __init__(self, interval=0.1, print_seconds=False, color: Optional[str] = None):
        """
        Args:
            interval=0.1 (float or int): The interval of refresh time for prints.
            print_seconds=True (bool): If false, prints oscillating slashes, else, prints seconds.
        """
        self._timer = None
        self._is_running = True
        self._interval = interval
        self._print_seconds = print_seconds
        self._color = color

    def _print(self, print_control_num: int):
        loading_msg = "\rRunning..."

        def p(s):
            return print(ColoredString(s, color=self._color).string, end='', flush=True)

        if not self._print_seconds:
            if print_control_num % 2:
                return p(f"{loading_msg}/")
            return p(f"{loading_msg}\\")
        return p(f"{loading_msg} {print_control_num / 10}")

    def _print_out_loading_msg(self):
        print_control_num = 0
        while self._is_running:
            self._print(print_control_num)
            print_control_num += 1
            sleep(self._interval)

    def start(self):
        self._timer = threading.Thread(target=self._print_out_loading_msg)
        self._timer.start()
        return self

    def stop(self):
        self._is_running = False


if __name__ == "__main__":
    import time

    print("TEST RUN FOR 5 SECONDS")

    tc = Tic(color=Colors.RED).start()
    time.sleep(5)
    tc.stop()
