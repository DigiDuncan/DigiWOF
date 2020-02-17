import random
import json
import importlib.resources as pkg_resources
from typing import Tuple

import digiwof.data
from digiwof.lib.constants import consonants, vowels, rounds

class Wedge:
    def __init__(self, value: int, *, special: str = None, toggleable: bool = None):
        if (not special and toggleable) or (not toggleable and special):
            raise SyntaxWarning
        self.value = value
        self.special = special
        self.toggleable = toggleable
        self._special_toggle = True if self.toggleable else None

    def disableSpecial(self):
        if special and toggleable:
            self._special_toggle = False


class Wheel:
    def __init__(self, wedges):
        self.wedges = wedges
        self.cursor = random.choice(self.wedges)

    def spin(self):
        self.cursor = random.choice(self.wedges)


class Player:
    __slots__ = ["name", "id", "total_score", "round_score", "tokens", "round_tokens"]
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.total_score = 0
        self.round_score = 0
        self.tokens = []
        self.round_tokens = []

    def mergeScore(self):
        self.total_score += self.round_score
        self.round_score = 0

    def addToken(self, token):
        self.round_tokens.append(token)

    def removeToken(self, token):
        self.round_tokens.remove(token)

    def mergeTokens(self):
        self.tokens += self.round_tokens
        self.round_tokens = []

    def bankrupt(self):
        self.round_score = 0
        self.round_tokens = []


class Board:
    def __init__(self, puzzle: str, category: str):
        self.puzzle = puzzle
        self.category = category
        self.tried_consonants = []
        self.tried_vowels = []
    
    @property
    def no_more_vowels(self):
        return set(self.puzzle).isdisjoint(vowels)

    def tryConsonant(self, c):
        if len(c) != 1:
            raise ValueError
        if c not in consonants:
            raise ValueError
        self.tried_consonants.append(c)

    def tryVowel(self, v):
        if len(v) != 1:
            raise ValueError
        if v not in vowels:
            raise ValueError
        self.tried_consonants.append(v)

    def reveal(self):
        self.tried_consonants = consonants
        self.tried_vowels = vowels

    def printBoard(self, linewidth):
        # TODO: Print a nice looking board.
        pass

class Game:
    def __init__(self, id: int, players: Tuple[Player, Player, Player]):
        self.id = id
        self.players = players
        self.wheels = self.wheelsFromJSON()
        self.puzzles = self.puzzlesFromJSON()
        self.prizes = self.prizesFromJSON()

        self.current_round_index = 0
        self.current_board = self.chooseBoard(self.current_round)
        self.current_wheel = self.getWheel(self.current_round)

    @property
    def current_round(self):
        # Start with the $1000 Toss Up.
        return rounds[self.current_round_index]

    @classmethod
    def wheelsFromJSON(cls):
        # TODO: Make a dictionary of round: Wheel.
        data = json.loads(pkg_resources.read_text(digiwof.data, "wheels.json"))

    @classmethod
    def puzzlesFromJSON(cls):
        return json.loads(pkg_resources.read_text(digiwof.data, "puzzles.json"))

    @classmethod
    def prizesFromJSON(cls):
        return json.loads(pkg_resources.read_text(digiwof.data, "prizes.json"))

    def nextRound(self):
        if self.current_round_index != len(rounds) - 1:
            self.current_round_index += 1

    def getWheel(self, round):
        # Toss-Up rounds are negative values, and use the same wheels as their positive counterparts.
        round = abs(round)
        return self.wheels[str(round)]

    def chooseBoard(self, round):
        if round < 0:
            round_type = "toss-up"
        elif round == 0:
            round_type = "bonus"
        elif 0 < round < 100:
            round_type = "normal"

        current_puzzle = random.choice(self.puzzles[round_type])
        return Board(current_puzzle["puzzle"], current_puzzle["category"])