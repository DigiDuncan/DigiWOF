from digiwof.lib.objects import Game, Player
from itertools import cycle

players = [
    Player("DigiDuncan"),
    Player("Natalie"),
    Player("Bob")
]
game = Game(players)
game.setup()

current_player = cycle([0, 1, 2])

while not game.round_over:
    game.do_turn(next(current_player))
