from threading import Timer

class TimeTicker:
    """A custom ticker that use a different thread to show if your interpreter is running.

    May or maynot relieve stress when waiting for a long function to run.

    Usage:
        1. Initialize the TimeTicker. This will start the timer.
        2. Stop the TimeTicker at a desired location.

    methods:
        stop: Stops TimeTicker.
    """
    def __init__(self, interval=0.1, no_seconds_display=True):
        """
        Args:
            interval=0.1 (float or int): The interval of refresh time for prints.
            no_seconds_display=True (bool): If true, prints oscillating slashes, else, prints seconds.
        """
        self._timer     = None
        self.interval   = interval
        self.use_ticks = no_seconds_display
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
            if self.use_ticks:
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
    # Initialization
    rt = TimeTicker(no_seconds_display=True)

    # Some long process that takes time...
    from time import sleep
    sleep(5)

    # The End
    rt.stop()