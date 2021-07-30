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
* **Solve the puzzle**: the player guesses the entire puzzle. If they get it right, they walk away with their current round earnings. If they get it wrong, they lose their turn.


### Special Round Types
#### $1000, $2000, and $3000 Toss-Up (-1, -2, -3)
The puzzle answer is revealed one letter at a time. Players can buzz in when they think they know the answer. When a Player buzzes in, they try to solve. Failing to give a correct answer locks out that Player for the rest of the Toss-Up.

The winner of the $2000 Toss-Up starts Round 1.

The winner of the $3000 Toss-Up starts Round 4.

#### Bonus Round (0)
The player with the most money at the end of the game moves on the Bonus Round. They spin the Bonus Wheel, but do not get to see what they landed on. They then solve a short puzzle. To do this, they are given the letters RSTLN and E for free, and they then choose three consonants and a vowel (four consonants if they possess a Wild Card.) They are then given 30 seconds<sup>1</sup> to solve the puzzle, with as many tries as they want. If they solve the puzzle, the prize is revealed and they receive it. If they fail, the prize is revealed regardless.

#### Final Spin (4)
The host spins the wheel once at the beginning of the round.<sup>2</sup> This plus $1000 is the value each consonant will be worth for the entirety of this round.
Each player's turn, they follow a two-phase process:
- **Either guessing a consonant or a vowel.** Consonants are worth the round's wedge value, and vowels are free.
- **Attempting to solve or passing.** There is no penalty for incorrect solves.

The round continues until the puzzle is solved.


### Special Wedges
#### Bankrupt
Lose all this round's tokens and money.
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

# Footnotes
<sup>1</sup> This may be too long.
<sup>1</sup> There may be a few spins before the "Final Spin" is done.
