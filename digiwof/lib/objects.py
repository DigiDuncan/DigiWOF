from digiwof.lib import constants
from digiwof.lib.utils import fit_to_board
import random
from typing import List


class Wedge:
    def __init__(self, value) -> None:
        self.value: int = 0


class Wheel:
    def __init__(self, wedges: List[Wedge]) -> None:
        self.wedges = wedges

        self.cursor = 0

    @property
    def current_wedge(self):
        return self.wedges[self.cursor]

    def spin(self) -> Wedge:
        self.cursor = random.randint(0, len(self.wedges) - 1)
        return self.current_wedge


class Board:
    def __init__(self, puzzle) -> None:
        self._display = fit_to_board(puzzle)
        if self._display is None:
            raise ValueError("Puzzle does not fit on board!")

        self.revealed_display = self._display
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            self.revealed_display = self.revealed_display.replace(letter, "#")

    def reveal(self, letter):
        for i, val in enumerate(self._display):
            if val == letter:
                self.revealed_display[i] = letter

    def reveal_all(self):
        self.revealed_display = self._display

    @property
    def emoji_board(self):
        newboard = ""
        for letter in self.revealed_display:
            if letter in constants.font:
                newboard += constants.font[letter]
            else:
                newboard += letter
        return newboard


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.score = 0
        self.round_score = 0
        self.inventory = []


class Game:
    def __init__(self, players: List[Player]) -> None:
        self.players = players

        self.puzzle: str = None
        self.used_letters = []
