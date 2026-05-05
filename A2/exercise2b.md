# AI2 Exercise 2b
#### Group 09: Wilhelm Oskar Ostermann, Marc Steger, Stefan Lepolt

## Answer Set Programming
#### Task A
For Task A, we defined several rules:
adjacent/4 takes two rows and cols as input and can be derived if the two positions on the grid are horizontally, vertically or diagonally adjacent.
allowed/2 takes a row and col as inputs and can be derived if the row and col are adjacent to a wall.
Then we placed light bulbs by "guessing" on allowed positions.
We then added a constraint that every valid position has to be litUp, for this we defined the rules litUp and blockedByRow/Col.
Result: clingo version 5.7.2 showed 801 correct models for the provided example instance of the grid.

#### Task B
For Task B, we just added one constraint and rule:
adjacentToWall/4 is self explanatory, it can be derived if one position is a wall and the other position is adjacent to it.
The constraint itself ensures with the aggregate function count that each wall doesnt have more than k light bulbs next to it.
Result: clingo version 5.7.2 showed 44 correct models for the provided example instance of the grid.
