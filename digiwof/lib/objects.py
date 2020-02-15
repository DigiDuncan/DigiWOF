import random
from digiwof.constants import consonants, vowels

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