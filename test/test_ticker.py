from ticker import TimeTicker

# main.py

if __name__=="__main__":
    # Initialization
    rt = TimeTicker(no_seconds_display=False)

    # Some long process that takes time...
    from time import sleep
    sleep(5)

    # The End
    rt.stop()

