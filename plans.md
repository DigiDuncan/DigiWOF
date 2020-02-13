# DigiWOF
## Objects

### Wedge
A Wedge object is a literal wedge on the wheel in the game. There are 24 of these on a Wheel.
#### Attributes
##### `Wedge.value` (int)
The amount of dollars represented by this wedge, or rather, how much money you will recieve per correct consonant if you are currently on this wedge.
##### `Wedge.special` (str?)
The name of the kind of special wedge this wedge is, if it is one. Might be `None`.
#### Methods/Functions
##### `__init__(value, special)`
Initialize a Wedge.
##### `turnOffSpecial()`
Turn the special on this wedge off, or, if this was the real game, take the special token off of this wedge.

### Wheel
The goal of the Wheel object is to represent the physical Wheel as seen in the game, which has a variety of Wedges on its face, and a "cursor" to select a Wedge. It also needs to remeber the "state" of some of these Wedges, as certain Wedges can have multiple peristent states.
#### Attributes
##### `Wheel.cursor` (Wedge)
The Wedge the wheel is currently pointing at.
##### `Wheel.wedges` (lst)
A list of Wedges the this wheel has on its "face".
#### Methods/Functions
##### `__init__(self, wedges)`
The only thing a Wheel needs to exist is its wedges.
Set the cursor to a random Wedge in `self.wedges` right away.
##### `spin()`
Spin the wheel, or, basically, set the cursor to a new random wedge.