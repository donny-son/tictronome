# Simple python tic that can ease your mind

We've all been there...staring at the empty terminal while your fans go crazy.  
I hope this relieves the intensity while you are waiting for that return statement.

<img src="assets/simple-tics.gif" width="250"/>
<!-- <img src="assets/seconds.gif" width="250"/> -->

## How To

0. Install `tictronome` from `pip`

```{shell}
$ pip install tictronome
```

1. Import `Tic` object from `tictronome`.

```{python}
from tictronome.tictronome import Tic
```

2. Initialize it before some time-consuming process.

```{python}
tic = Tic()
```

3. Call the `start` method of `Tic` to start.

```{python}
# start of your script
tic.start()
some_long_function(...)
```

3. Call the `stop` method of `Tic` to stop.

```{python}
# end of your script
tic.stop()
```

4. Run your script!

```{shell}
$ python3 your_script.py
```

### Notes

When you create a Tic instance, you can change the color of the loading character by adding colors.

**_Disclaimer_**

Depending on your shell settings(themes) colors might appear differently.

```{python}
from tictronome import Colors
Tic(color=Colors.CYAN)
```

![color_example](./assets/color_example.png)

| Supported List of Colors
| :---:
| Colors.BLACK
| Colors.RED
| Colors.GREEN
| Colors.YELLOW
| Colors.BLUE
| Colors.MAGENTA
| Colors.CYAN
| Colors.WHITE
