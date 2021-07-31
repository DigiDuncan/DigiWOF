from digiwof.lib import constants
from digiwof.lib.utils import fit_to_board
import random
from typing import List
import time


class Wedge:
    def __init__(self, value) -> None:
        self.value: int = value


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

    def reveal(self, letter) -> int:
        count = 0
        for i, val in enumerate(self._display):
            if val == letter:
                self.revealed_display = self.revealed_display[:i] + letter + self.revealed_display[i + 1:]
                count += 1
        return count

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

    @property
    def complete(self):
        return "#" not in self.revealed_display


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.score = 0
        self.round_score = 0
        self.inventory = []

    def get_choice(self, choices: list):
        print(f"{self.name}: {choices}")
        choice = random.choice(choices)
        print(f"Choice: {choice}")
        return choice

    def ask_for_consonant(self) -> str:
        print(f"{self.name}: Choose a consonant!")
        consonant = random.choice("BCDFGHJKLMNPQRSTVWXYZ")
        print(f"Consonant: {consonant}")
        return consonant

    def get_response(self) -> str:
        print(f"{self.name}: Respond!")
        response = "".join([random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ ") for i in range(20)])
        print(f"Response: {response}")
        return response


class Game:
    def __init__(self, players: List[Player]) -> None:
        self.players = players

        self.puzzle: str = None
        self.used_letters = []
        self.used_vowels = []
        self.round_over = False

    def no_more_vowels(self):
        vowels = ["A", "E", "I", "O", "U"]
        untried_vowels = list(set(vowels) - set(self.used_vowels))
        for v in untried_vowels:
            if v in self.puzzle:
                return False
        print("There are no more vowels!")
        return True

    def tried_all_consonants(self):
        if "BCDFGHJKLMNPQRSTVWXYZ" == "".join(sorted(self.used_letters)):
            print("There are no more consonants!")
            return True
        return False

    def setup(self):
        self.puzzle = "THIS IS A PUZZLING PUZZLE"
        wedges = [Wedge(500)] * 12 + [Wedge(1000)] * 12
        self.wheel = Wheel(wedges)
        self.board = Board(self.puzzle)

    def player_wins(self, player):
        self.board.reveal_all()
        for p in self.players:
            if p != player:
                p.round_score = 0
        print(f"{player.name} wins the round!")
        self.round_over = True

    def get_consonant(self, player: Player):
        consonant = None
        while consonant is None:
            consonant = player.ask_for_consonant()
            if consonant in self.used_letters:
                print(f"We've already tried {consonant}")
                consonant = None
        return consonant

    def get_vowel(self, player: Player):
        vowel = None
        while vowel is None:
            vowel = player.get_choice(["A", "E", "I", "O", "U"])
            if vowel in self.used_vowels:
                print(f"We already tried {vowel}!")
                vowel = None
        return vowel

    def do_turn(self, player_num: int):
        print(self.board.revealed_display)
        player = self.players[player_num]
        print(f"{player.name}: ${player.round_score}")
        choice_made = False
        while not choice_made:
            choice = player.get_choice(["spin", "vowel", "solve"])
            if choice == "vowel" and player.round_score < 250:
                print("You don't have enough money to buy a vowel!")
            elif choice == "vowel" and self.no_more_vowels():
                continue
            elif choice == "spin" and self.tried_all_consonants():
                continue
            else:
                choice_made = True
        if choice == "spin":
            wedge = self.wheel.spin()
            value = wedge.value
            choice = self.get_consonant(player)
            count = self.board.reveal(choice)
            print(f"There are {count} {choice}s!")
            self.used_letters.append(choice)
            player.round_score += value * count
        elif choice == "vowel":
            choice = self.get_vowel(player)
            count = self.board.reveal(choice)
            player.round_score -= 250
            print(f"There are {count} {choice}s!")
            self.used_vowels.append(choice)
        elif choice == "solve":
            solve = player.get_response()
            if solve == self.puzzle:
                self.player_wins(player)
            else:
                print("Sorry, that's wrong.")

        if self.board.complete:
            self.player_wins(player)

        time.sleep(1)
