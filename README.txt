Documentation of Rush Hour Game
ECE 2524 - Project 3
By Noah Davis and Aparajita (Pia) Banerjee

OBJECTIVE
Similar to the classic arcade game, our Rush Hour game follows the same idea. The player must have a particular car pass through the 'Exit' 
while trying to get by the other cars on its way. The player can only perform a legal move horizontally or vertically, and cannot go over 
another car, nor 'jump' over to a different spot. 

LAYOUT
For our Python-implemented game, we decided to keep a grid-style layout which would have a co-ordinate system. On the top, the grid is 
arranged alphabetically in uppercase (i.e. x-axis) and the y-axis is denoted in lower-case alphabets. The following is an example grid 
of the 'easy' level of the game. 

   A  B  C  D  E  F
   -------------------
 a |  |  |  |  |  |11|
   -------------------
 b |  |  |  |  |  |11|
   ----------------------
 c |  |  |  |00|00|11  Exit
   ----------------------
 d |  |  |  |  |  |  |
   -------------------
 e |  |  |  |33|22|22|
   -------------------
 f |  |  |  |33|  |  |
   -------------------
 
As shown above, the cars are numbered as 00, 11, 22 and onwards. They could either be 2 or 3-spaced in length. Notice the difference 
between 00 and 11. 
Each point will be denoted in the order of X-axis, followed by the Y-axis, just like an ordinary cordinate system. 

Example: 
- Horizontally: First possible point will be Aa, followed by Ba, Ca and so on directly on the right-side.
- Vertically: First possible point will be Aa, followed by Ab, Ac and so on directly down.

HOW TO START AND PLAY THE GAME? 
1) Start up Terminal

2) Go to the directory that contains the file contents of the game

3) Type the following to start the game:
	$ python3 ./main.py

4) Player will first be asked to enter level of difficulty for the game. Type either: 
	$ easy
   OR	$ medium
   OR 	$ hard
   and hit the enter key

5) Player will now be shown a 'map' of cars that they will have to play with in the game. Type the car number that needs to be moved. 
Example: 00, 11, 22, etc.

6) Player will then be asked about the co-ordinate that they want to move that car to. For a horizontal move, the player must look at the 
right-most side of the car and make the judgment. For a vertical move, the player must look at the upper-most side of the car and make the 
appropriate judgment.
Example: Ab, Bd, etc.

7)Player keeps repeating Steps 5 and 6 to win the game (i.e trying to get the car into point Fc to win). A surprise awaits right after the 
win!

