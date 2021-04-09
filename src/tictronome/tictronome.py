from threading import Timer

class Tic:
    """Different thread to show if your interpreter is running.

    May or maynot relieve stress when waiting for a long function to run.

    Usage:
        1. Initialize the Tic. This will start the timer.
        2. Stop the Tic at a desired location.

    methods:
        stop: Stops Tic.
    
    Example:
        >>> from tic import Tic  # import Tic class
        >>> tic = Tic(0.1, print_seconds=False)  # initialize before a long function call
        >>> some_long_function_to_process(...)  # the long function call
        >>> tic.stop()  # end of script or wherever you want it to end
        
    """
    def __init__(self, interval=0.1, print_seconds=False):
        """
        Args:
            interval=0.1 (float or int): The interval of refresh time for prints.
            print_seconds=True (bool): If false, prints oscillating slashes, else, prints seconds.
        """
        self._timer = None
        self.interval = interval
        self.print_seconds = print_seconds
        self.is_running = False
        self.time = 0
        self._start()

    def _run(self):
        self.is_running = False
        self._start()

    def _start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.time += 1
            if not self.print_seconds:
                if self.time % 2:
                    print("Running", '/', end="\r", sep="...", flush=True)
                else:
                    print("Running", '\\', end="\r", sep="...", flush=True)
            else:
                    print("Seconds Passed", self.time / 10, end="\r", sep="...", flush=True)
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False


if __name__=="__main__":
    print("TEST RUN FOR 5 SECONDS")

    tc = Tic()
    import time
    time.sleep(5)
    
    tc.stop()