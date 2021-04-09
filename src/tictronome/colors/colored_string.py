from .ansi import Fore, Style
from typing import Optional


class Colors:
    BLACK = "BLACK"
    RED = "RED"
    GREEN = "GREEN"
    YELLOW = "YELLOW"
    BLUE = "BLUE"
    MAGENTA = "MAGENTA"
    CYAN = "CYAN"
    WHITE = "WHITE"


class ColoredString:
    def __init__(self, s: str, color: Optional[str] = None):
        self._color = color
        self._s = s

    @property
    def string(self) -> str:
        if self._color is None:
            return self._s
        return f"{getattr(Fore, self._color )} {self._s} {Fore.RESET} {getattr(Style, 'NORMAL')}"


