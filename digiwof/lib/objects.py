from digiwof.lib.utils import fit_to_board
import random
from typing import List


class Wedge:
    def __init__(self) -> None:
        self.value: int = 0
        self.special: str = None
        self.togglable: bool = None
        self.toggled: bool = None

    def special_function(self, player):
        raise NotImplementedError


class Wheel:
    def __init__(self, puzzle: str, wedges: List[Wedge]) -> None:
        self.puzzle = puzzle

        if fit_to_board(self.puzzle) is None:
            raise ValueError("Puzzle does not fit on board!")

        self.wedges = wedges

        self.cursor = 0
        self.used_letters = []

    @property
    def current_wedge(self):
        return self.wedges[self.cursor]

    def spin(self) -> Wedge:
        self.cursor = random.randint(0, len(self.wedges) - 1)
        return self.current_wedge
