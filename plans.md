# DigiWOF
## Objects

### Wedge
A Wedge object is a literal wedge on the wheel in the game. There are 24 of these on a Wheel. It also needs to remeber the "state" of some of these Wedges, as certain Wedges can have multiple peristent states.

#### Attributes
##### `Wedge.value` (int)
The amount of dollars represented by this wedge, or rather, how much money you will recieve per correct consonant if you are currently on this wedge.
##### `Wedge.special` (str?)
The name of the kind of special wedge this wedge is, if it is one. Might be `None`.

#### Methods/Functions
##### `__init__(self, value: int, special: str)`
Initialize a Wedge.
##### `turnOffSpecial()`
Turn the special on this wedge off, or, if this was the real game, take the special token off of this wedge.


### Wheel
The goal of the Wheel object is to represent the physical Wheel as seen in the game, which has a variety of Wedges on its face, and a "cursor" to select a Wedge.

#### Attributes
##### `Wheel.cursor` (Wedge)
The Wedge the wheel is currently pointing at.
##### `Wheel.wedges` (lst)
A list of Wedges the this wheel has on its "face".

#### Methods/Functions
##### `__init__(self, wedges: lst)`
The only thing a Wheel needs to exist is its wedges.
Set the cursor to a random Wedge in `self.wedges` right away.
##### `spin()`
Spin the wheel, or, basically, set the cursor to a new random wedge.


### Player
The Player is a person who is playing the game. They keep track of their own total score, current round score, current round tokens they are holding, and persistent tokens they have.

#### Attributes
##### `Player.name` (str)
The players name. Very literal.
##### `Player.id` (int)
A unique ID for the player. Shouldn't overlap with any other player. If we're doing a Discord frontend for this, use their Discord ID so you can match up the player to a Discord ID. If you try to add two players with the same ID to a Game, the Game should probably throw an error.
##### `Player.total_score` (jnt)
The player's current total score. If the game were to end right now, this is what they'd "walk away" with.
##### `Player.round_score` (int)
The player's running score for the current round.
##### `Player.tokens` (lst)
The tokens a player has collected and kept across rounds.
##### `Player.round_tokens` (lst)
The tokens a player has this round. These would get wiped with a Bankrupt.

#### Methods/Functions
##### `__init__(self, name: str, id: int)`
In theory, the only things you should need to make a Player is their name, and a unique ID.
##### `addTotal(x: int)`
Add `x` to the Player's `total_score` directly.
##### `addScore(x: int)`
Add `x` to the Player's `round_score`. (accepts negatives for subtraction.)
##### `mergeScore()`
Add the Player's `round_score` to their `total_score`.
##### `addToken(token: ?)`<sup>*</sup>
Add `token` to the Player's `round_tokens`.
##### `removeToken(token: ?)`<sup>*</sup>
Remove `token` from the Player's `round_tokens`.
##### `mergeTokens()`
Merge the Player's `round_tokens` list into their `tokens` list.
##### `bankrupt()`
A shortcut function: set the Player's `round_score` to 0, and clear their `round_tokens` list.

### Board
The Board represents the physical board in the game: it has a puzzle displayed on it in varying states of reveal. It also stores a category.

#### Attributes
##### `Board.puzzle` (str)
The final, solved puzzle. i.e.: the word(s) that are the solution to this round.
##### `Board.category` (str)
The category of the puzzle on this board.
##### `Board.tried_consonants` (lst)
A list of the consonants that have been tried already.
##### `Board.tried_vowels` (lst)
A list of the vowels that have been tried already.
##### `Board.no_more_vowels` (bool)
True if there are no more vowels in the puzzle that are hidden.

#### Methods/Functions
##### `__init__(self, puzzle: str, category: str)`
Create a Board with a puzzle and a category.
##### `try_consonant(c: chr)`
Add a consonant `c` to the `tried_consonants` list.
##### `try_vowel(v: chr)`
Add a vowel `v` to the `tried_vowels` list.
##### `reveal()`
Add all possible consonants/vowels to the `tried_consonants` and `tried_vowels` list, essentially revealing the whole puzzle.

### Round
The Round contains the current Board and the current Wheel.

#### Attributes
##### `Round.round_type` (int)
What kind of round this is. Either 1, 2, 3, or 4 for Rounds 1-4, 0 for a Toss-Up, or -1 for the Bonus Round.
##### `Round.board` (Board)
The board currently being played on this round.
##### `Round.wheel` (Wheel)
The wheel currently being spun this round.

#### Methods/Functions
##### `__init__(self, round_type: int, wheels: dict, puzzles: dict)`
Creates a round of `round_type`, and create a wheel that matches that round type by reading the wheels dict and creating a wheel that matches the round type, and creates a Board with a random puzzle (from the puzzles dict) of that round type.

### Game
???

#### Attributes
???

#### Methods/Functions
##### `__init__(self, players, wheels, puzzles, prizes)`<sup>?</sup>
???

## Gameplay
* $1,000 Toss-Up
* \[interviews\]
* $2,000 Toss-Up
* Round 1
* \[commerical break\]
* Round 2
* \[commerical break\]
* Round 3
* \[commerical break\]
* $3,000 Toss-Up
* Round 4 (Final Spin)
* \[commerical break\]
* Bonus Round

## Special Wedges
### Backrupt
Lose all this round tokens and money.
### Lose A Turn
The turn moves on to the next turn.
### Mystery
Is at its face a $1000 wedge, but if the player chooses, they can flip it over for a 50/50 shot of it being either a Bankrupt or $10K.
### 1/2 Car
Collect two of the 1/2 Car tokens for a car prize.
### Wild
If a Player correctly guess a consonant on the Wedge containing a Wild token, they have three options:
- Use it immediately: this allows them to guess another consonant, and each correct consonant is worth \[wedge value\] + $500.
- Use it on another turn: this allows them to guess another consonant, and each correct consonant is worth \[wedge value\].
- Take it to the bonus round: this allows them to guess an extra consonant, on top of the standard three consonants and a vowel.

Wild cards are edible. <sup>[\[1\]](https://www.youtube.com/watch?v=_HphjRFOHPI)</sup>
### One Million
Has either a 2/3 chance of being a Bankrupt, or a 1/3 chance of giving the Player a "million dollar" token on a correct guess. This is taken to the Bonus round and replaces one of the envelopes on the Bonus Wheel with a million-dollar envelope.
### Free Play
Free Play allows Players to call a letter,call a free vowel, or solve the puzzle right
away, all without penalty. Aside from this, Free Play acts as a $500 wedge and correct consonants are worth $500 each.
### Gift
The Gift Tag offers $1,000 towards a company's products, plus $500 per consonant.
### Prize
If the Player correctly guesses a consonant on this wedge, they pick up the Prize token. If they hold the Prize token at the end of the round, they get the prize. The Prize wedge is obscuring a $500 wedge.
### Express
**From** ***wheeloffortunehistory.fandom.com***:

> *Placed on the red $700 in Round 3, the Express offers a "face value" of $1,000; if a contestant lands on it and calls a correct letter, they may either take another regular turn or risk their current earnings to "hop aboard the Express" by continuing to call correct letters, earning $1,000 per consonant. The player may also buy vowels, which still cost $250. Unlike flipping the Mystery Wedge hiding a prize, the contestant does not forfeit his/her earnings to hop onboard the Express.*

> *The player remains on the Express until they solve the puzzle or lose their turn, the latter of which also acts as a Bankrupt (and plays the slide whistle). Should a player go Bankrupt on Express, the wedge is still kept in play, thus allowing the possibility of more than one Express run in a game.*

This is not planned to be implemented.