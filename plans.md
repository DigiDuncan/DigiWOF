# DigiWOF
## Gameplay

This section is meant to describe the game play format of the game, but in doing so accidentally is a decent overview of the game *Wheel of Fortune*.

The goal of Wheel of Fortune is to solve Hangman-style word puzzles to win money.

### Format
* $1,000 Toss-Up
* \[interviews\]
* $2,000 Toss-Up
* Round 1
* \[commercial break\]
* Round 2
* \[commercial break\]
* Round 3
* \[commercial break\]
* $3,000 Toss-Up
* Round 4 (Final Spin)
* \[commercial break\]
* Bonus Round


### Normal Rounds

During a normal round, a Player spins the Wheel. Depending on what the land on, multiple things can happen. (See [Special Wedges](#special-wedges).) Assuming the Player lands on a "normal wedge" (one with a dollar value on its face), the player can choose to do one of three things:

* **Guess a consonant**: the player guesses a consonant, and if it's on the board, they receive [wedge value] x [number of consonants on the board].
* **Buy a vowel**: the player spends $250 to reveal one of five vowels from the puzzle. (This costs money even if the vowel isn't there.)
* **Solve the puzzle**: the player guesses the entire puzzle. If they get it right, they walk away with their current round earnings, and the second and third place Players walk away from that round with $2000 and $1000, respectively. If they get it wrong, they lose their turn.


### Special Round Types
#### $1000, $2000, and $3000 Toss-Up (-1, -2, -3)
The puzzle answer is revealed one letter at a time. Players can buzz in when they think they know the answer. When a Player buzzes in, they try to solve. Failing to give a correct answer locks out that Player for the rest of the Toss-Up.

The winner of the $1000 Toss-Up starts Round 1.

The winner of the $3000 Toss-Up starts Round 4.
#### Bonus Round (0)
The player with the most money at the end of the game moves on the Bonus Round. They spin the Bonus Wheel, but do not get to see what they landed on. The then solve a short puzzle. To do this, they are given the letters RSTLN and E for free, and they then choose three consonants and a vowel (four consonants if they possess a Wild Card.) They are then given 30 seconds to solve the puzzle, with as many tries as they want. If they solve the puzzle, the prize is revealed and they receive it. If they fail, the prize is revealed regardless.

#### Final Spin (4)
The host spins the wheel once at the beginning of the round. This is the value each consonant will be worth for the entirety of this round.
Each player's turn, they follow a two-phase process:
- **Either guessing a consonant or a vowel.** Consonants are worth the round's wedge value, and vowels are free.
- **Attempting to solve or passing.** There is no penalty for incorrect solves.

The round continues until the puzzle is solved.


### Special Wedges
#### Bankrupt
Lose all this round tokens and money.
#### Lose A Turn
The turn moves on to the next turn.
#### Mystery
Is at its face a $1000 wedge, but if the player chooses, they can flip it over for a 50/50 shot of it being either a Bankrupt or $10K.
#### 1/2 Car
Collect two of the 1/2 Car tokens for a car prize.
#### Wild
If a Player correctly guess a consonant on the Wedge containing a Wild token, they have three options:

- **Use it immediately**: this allows them to guess another consonant, and each correct consonant is worth \[wedge value\] + $500.
- **Use it on another turn**: this allows them to guess another consonant, and each correct consonant is worth \[wedge value\].
- **Take it to the bonus round**: this allows them to guess an extra consonant, on top of the standard three consonants and a vowel.

Wild cards are edible. <sup>[\[1\]](https://www.youtube.com/watch?v=_HphjRFOHPI)</sup>
#### One Million
Has either a 2/3 chance of being a Bankrupt, or a 1/3 chance of giving the Player a "million dollar" token on a correct guess. This is taken to the Bonus round and replaces one of the envelopes on the Bonus Wheel with a million-dollar envelope.
#### Free Play
Free Play allows Players to call a letter, call a free vowel, or solve the puzzle right away, all without penalty. Aside from this, Free Play acts as a $500 wedge and correct consonants are worth $500 each.
#### Gift
The Gift Tag offers $1,000 towards a company's products, plus $500 per consonant.
#### Prize
If the Player correctly guesses a consonant on this wedge, they pick up the Prize token. If they hold the Prize token at the end of the round, they get the prize. The Prize wedge is obscuring a $500 wedge.
#### Express
**From** ***wheeloffortunehistory.fandom.com***:

> *Placed on the red $700 in Round 3, the Express offers a "face value" of $1,000; if a contestant lands on it and calls a correct letter, they may either take another regular turn or risk their current earnings to "hop aboard the Express" by continuing to call correct letters, earning $1,000 per consonant. The player may also buy vowels, which still cost $250. Unlike flipping the Mystery Wedge hiding a prize, the contestant does not forfeit his/her earnings to hop onboard the Express.*

> *The player remains on the Express until they solve the puzzle or lose their turn, the latter of which also acts as a Bankrupt (and plays the slide whistle). Should a player go Bankrupt on Express, the wedge is still kept in play, thus allowing the possibility of more than one Express run in a game.*

This is not planned to be implemented.


## Objects


### Wedge
A Wedge object is a literal wedge on the wheel in the game. There are 24 of these on a Wheel. It also needs to remember the "state" of some of these Wedges, as certain Wedges can have multiple persistent states.

#### Attributes
##### `Wedge.value` (int)
The amount of dollars represented by this wedge, or rather, how much money you will receive per correct consonant if you are currently on this wedge.
##### `Wedge.special` (str?)
The name of the kind of special wedge this wedge is, if it is one. Might be `None`.

#### Methods/Functions
##### `__init__(self, value: int, *, special: str = None, toggleable: bool = None)`
Initialize a Wedge.
##### `disableSpecial()`
Turn the special on this wedge off, or, if this was the real game, take the special token off of this wedge.


### Wheel
The goal of the Wheel object is to represent the physical Wheel as seen in the game, which has a variety of Wedges on its face, and a "cursor" to select a Wedge.

#### Attributes
##### `Wheel.cursor` (Wedge)
The Wedge the wheel is currently pointing at.
##### `Wheel.wedges` (list)
A list of Wedges the this wheel has on its "face".

#### Methods/Functions
##### `__init__(self, wedges: list)`
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
##### `Player.total_score` (int)
The player's current total score. If the game were to end right now, this is what they'd "walk away" with.
##### `Player.round_score` (int)
The player's running score for the current round.
##### `Player.tokens` (list)
The tokens a player has collected and kept across rounds.
##### `Player.round_tokens` (list)
The tokens a player has this round. These would get wiped with a Bankrupt.

#### Methods/Functions
##### `__init__(self, name: str, id: int)`
In theory, the only things you should need to make a Player is their name, and a unique ID.
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
##### `Board.tried_consonants` (list)
A list of the consonants that have been tried already.
##### `Board.tried_vowels` (list)
A list of the vowels that have been tried already.
##### `Board.no_more_vowels` (bool)
True if there are no more vowels in the puzzle that are hidden.

#### Methods/Functions
##### `__init__(self, puzzle: str, category: str)`
Create a Board with a puzzle and a category.
##### `tryConsonant(c: chr)`
Add a consonant `c` to the `tried_consonants` list.
##### `tryVowel(v: chr)`
Add a vowel `v` to the `tried_vowels` list.
##### `reveal()`
Add all possible consonants/vowels to the `tried_consonants` and `tried_vowels` list, essentially revealing the whole puzzle.
##### `printBoard(linewidth: int)`
Print the board, with the correct letters revealed, and fitting in a line width of `linewidth`.


### Game
Represents an entire Game.

#### Attributes
##### `Game.id` (int)
A unique ID for this game.
##### `Game.players` (Tuple[Player, Player, Player])
A tuple containing the three player objects for this game.
##### `Game.wheels` (Tuple[Wheel, Wheel, Wheel, Wheel, Wheel])
A tuple containing the five wheel objects for this game, in the order Bonus, Round 1, Round 2, Round 3, Rpund 4.
##### `Game.puzzles` (dict)
A dictionary of lists of dictionaries representing puzzles, according to `puzzles.json`.
##### `Game.prizes` (dict)
A dictionary of prize: value.
##### `Game.cars` (dict)
A dictionary of car: value.
##### `Game.current_round_index` (int)
A zero-indexed integer tat increments every round.
##### `Game.current_round` (int)
The round type ID of the current round.
##### `Game.current_board` (Board)
The Board object currently in use in the game.
##### `Game.current_wheel` (Wheel)
The Wheel object currently in use in the game.

#### Methods/Functions
##### `__init__(self, id: int, players: (Tuple[Player, Player, Player])`
Start a new Game.
##### `wheelsFromJSON(cls)`
##### `puzzlesFromJSON(cls)`
##### `prizesFromJSON(cls)`
Converts the `wheels.json`. `puzzles.json`, and `prizes.json` files into usable data.
##### `nextRound(self)`
Increments the `Game.current_round_index` if it can.
##### `getWheel(self, round: int)`
Returns a Wheel that matches the current round.
##### `chooseBoard(self, round: int)`
Returns a Board that matches the current round.


## Visual Representations

### Main Screen (example)
![Example of the main screen.](https://cdn.discordapp.com/attachments/658894731623006229/678389354007363604/2020-02-15_18_56_29-Window.png)
```
<:blank:665063842866397185><:blank:665063842866397185><:blank:665063842866397185><:blank:665063842866397185>`*** Wheel of Fortune ***`<:blank:665063842866397185><:blank:665063842866397185><:blank:665063842866397185><:blank:665063842866397185>
⬜⁠⬜⁠⬜⁠⬜⁠⬜⁠⬜⁠⬜⁠⬜⁠⬜⁠⬜⁠⬜⁠⬜⁠⬜⁠⬜⁠⬜⁠
⬜⁠⬜⁠⬜⁠⬜⁠🇩⁠🟦⁠🟦⁠🟦⁠🇴⁠🟦⁠🇩⁠⬜⁠⬜⁠⬜⁠⬜
⬜⁠⬜⁠⬜⁠⬜⁠🟦⁠🇴⁠🟦⁠⬜⁠⬜⁠⬜⁠⬜⁠⬜⁠⬜⁠⬜⁠⬜
⬜⁠⬜⁠⬜⁠⬜⁠⬜⁠⬜⁠⬜⁠⬜⁠⬜⁠⬜⁠⬜⁠⬜⁠⬜⁠⬜⁠⬜
⬜⁠⬜⁠⬜⁠⬜⁠⬜⁠⬜⁠⬜⁠⬜⁠⬜⁠⬜⁠⬜⁠⬜⁠⬜⁠⬜⁠⬜
<:blank:665063842866397185><:blank:665063842866397185><:blank:665063842866397185><:blank:665063842866397185><:blank:665063842866397185><:blank:665063842866397185><:blank:665063842866397185>`Category: Thing`<:blank:665063842866397185><:blank:665063842866397185><:blank:665063842866397185><:blank:665063842866397185><:blank:665063842866397185><:blank:665063842866397185><:blank:665063842866397185>
🟥⁠🟥⁠🟥⁠🟥⁠🟥⁠🟨⁠🟨⁠🟨⁠🟨⁠🟨⁠🟦⁠🟦⁠🟦⁠🟦⁠🟦
`    Kelly    |    Natalie    |  DigiDuncan  `
`    $3000    |     $2000     |    $1999     `
🟥⁠🟥⁠🟥⁠🟥⁠🟥⁠🟨⁠🟨⁠🟨⁠🟨⁠🟨⁠🟦⁠🟦⁠🟦⁠🟦⁠🟦
`Tried Letters: B|D|E|O|P`
`Current Wedge: $750`
```