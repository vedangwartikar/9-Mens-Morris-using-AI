# CS 6364 - Final Project Report - Vedang Wartikar (VPW210000)

## 1. How to execute
### About
<pre>
Usage: <b>python3 <_FILE_NAME_>.py board1.txt board2.txt depth [-h] [--print_board [print_board]]</b>

Generates the next move for the White/Black player using MiniMax and Alpha-Beta Pruning algorithms

positional arguments:
  board1.txt            Input File Name
  board2.txt            Output File Name
  depth                 Depth of the search tree

optional arguments:
  -h, --help            show this help message and exit
  --print_board [print_board]
                        Print the board
</pre>

### Example
  - The program should be run in the following manner
    
  <pre>
  ╰─ cat board1.txt
  xxxxxxxxxxxxxxxxxxxxx
  ╰─ python3 MiniMaxOpening.py board1.txt board2.txt 2
  Board Position: Wxxxxxxxxxxxxxxxxxxxx.
  Positions evaluated by static estimation: 420.
  MINIMAX estimate: 0.
  </pre>

  - It can also be run with an optional parameter _--print_board_ for a visual representation of the board after a move has been played
  
  <pre>
  ╰─ cat board1.txt
  xxxxxxxxxxxxxxxxxxxxx
  ╰─ python3 MiniMaxOpening.py board1.txt board2.txt 2 --print_board
  Input Board:
  x--------x--------x
  |        |        |
  |  x-----x-----x  |
  |  |     |     |  |
  |  |  x--x--x  |  |
  |  |  |     |  |  |
  x--x--x     x--x--x
  |  |  |     |  |  |
  |  |  x-----x  |  |
  |  |           |  |
  |  x-----------x  |
  |                 |
  x-----------------x
  Output Board:
  x--------x--------x
  |        |        |
  |  x-----x-----x  |
  |  |     |     |  |
  |  |  x--x--x  |  |
  |  |  |     |  |  |
  x--x--x     x--x--x
  |  |  |     |  |  |
  |  |  x-----x  |  |
  |  |           |  |
  |  x-----------x  |
  |                 |
  W-----------------x
  Board Position: Wxxxxxxxxxxxxxxxxxxxx.
  Positions evaluated by static estimation: 420.
  MINIMAX estimate: 0.
  </pre>

## 2. MiniMax Algorithm
### Opening Phase
- After running the `opening_simulator.sh` which simulates the 8 moves using the MiniMax algorithm for White and Black players consecutively, we get the following board. Here we can see that the White player was able to form a (vertical) mill and take out one of the Black player's pieces. The Black player was also able to block 2 potential mills of the White player.
<pre>
Input Board:
B--------x--------x
|        |        |
|  W-----x-----W  |
|  |     |     |  |
|  |  x--x--x  |  |
|  |  |     |  |  |
W--W--B     W--B--x
|  |  |     |  |  |
|  |  W-----B  |  |
|  |           |  |
|  W-----------B  |
|                 |
W-----------------B
Output Board:
B--------x--------x
|        |        |
|  W-----B-----W  |
|  |     |     |  |
|  |  x--x--x  |  |
|  |  |     |  |  |
W--W--B     W--B--x
|  |  |     |  |  |
|  |  W-----B  |  |
|  |           |  |
|  W-----------B  |
|                 |
W-----------------B
Board Position: WBWBWBWWBWBxxxxWBWBxx.
Positions evaluated by static estimation: 78.
MINIMAX estimate: 2.
</pre>

### Midgame and EndGame
- In the following example, the White player closes a mill by moving its piece and removes a Black piece from the bottom right
<pre>
╰─ cat board1.txt
xBWBxWBBxxBBxWxWxBBWW
╰─ python3 MiniMaxGame.py board1.txt board2.txt 2 --print_board
Input Board:
B--------W--------W
|        |        |
|  W-----x-----B  |
|  |     |     |  |
|  |  x--W--x  |  |
|  |  |     |  |  |
B--B--x     x--B--B
|  |  |     |  |  |
|  |  x-----W  |  |
|  |           |  |
|  W-----------B  |
|                 |
x-----------------B
Output Board:
B--------W--------W
|        |        |
|  x-----W-----B  |
|  |     |     |  |
|  |  x--W--x  |  |
|  |  |     |  |  |
B--B--x     x--B--B
|  |  |     |  |  |
|  |  x-----W  |  |
|  |           |  |
|  W-----------B  |
|                 |
x-----------------x
Board Position: xxWBxWBBxxBBxWxxWBBWW.
Positions evaluated by static estimation: 90.
MINIMAX estimate: -1017.
</pre>

## 3. Alpha-Beta Pruning Algorithm
### Opening Phase
- For the following input board, the MiniMax and Alpha-Beta Pruning algorithms (ply 3) smartly place the White player's piece on the top right corner making it a possibility of at least 1 mill irrespective of the Black player's next move. The **positions evaluated by the static estimation function** and the **Minimax estimate** have been compared for both algorithms. We can clearly see that Alpha-Beta Pruning is very efficient in minimizing the unnecessary computations done by the MiniMax algorithm.
<pre>
╰─ cat board1.txt
xxWBxBxxxxxWxxWxBxWxx
╰─ python3 MiniMaxOpening.py board1.txt board2.txt 3 --print_board
Input Board:
W--------x--------x
|        |        |
|  x-----B-----x  |
|  |     |     |  |
|  |  x--x--W  |  |
|  |  |     |  |  |
x--x--x     x--x--W
|  |  |     |  |  |
|  |  x-----B  |  |
|  |           |  |
|  W-----------B  |
|                 |
x-----------------x
Output Board:
W--------x--------W
|        |        |
|  x-----B-----x  |
|  |     |     |  |
|  |  x--x--W  |  |
|  |  |     |  |  |
x--x--x     x--x--W
|  |  |     |  |  |
|  |  x-----B  |  |
|  |           |  |
|  W-----------B  |
|                 |
x-----------------x
  
-------- MiniMax Algorithm --------
Board Position: xxWBxBxxxxxWxxWxBxWxW.
Positions evaluated by static estimation: 2616.
MINIMAX estimate: 3.
  
-------- Alpha-Beta Pruning --------
Board Position: xxWBxBxxxxxWxxWxBxWxW.
Positions evaluated by static estimation: 875.
MINIMAX estimate: 3.
</pre>

### MidGame and Endgame Phase
- For the following input board, the MiniMax and Alpha-Beta Pruning algorithms (ply 5) the White player's piece at position 3 is moved to the top. The move is fairly simple, but as seen below the positions evaluated by Alpha-Beta Pruning are **360** and that of MiniMax is **4643**. Therefore, **Alpha-Beta is 13x more efficient that the MiniMax** algorithm in terms if the positions being evaluated.
<pre>
╰─ cat board1.txt
BBWWWxWBBxxxWWBWWBxBB
╰─ python3 ABGame.py board1.txt board2.txt 5 --print_board
Input Board:
x--------B--------B
|        |        |
|  W-----W-----B  |
|  |     |     |  |
|  |  W--W--B  |  |
|  |  |     |  |  |
W--B--B     x--x--x
|  |  |     |  |  |
|  |  W-----x  |  |
|  |           |  |
|  W-----------W  |
|                 |
B-----------------B
Output Board:
x--------B--------B
|        |        |
|  W-----W-----B  |
|  |     |     |  |
|  |  W--W--B  |  |
|  |  |     |  |  |
W--B--B     x--W--x
|  |  |     |  |  |
|  |  W-----x  |  |
|  |           |  |
|  W-----------x  |
|                 |
B-----------------B
  
-------- MiniMax Algorithm --------
Board Position: BBWxWxWBBxWxWWBWWBxBB.
Positions evaluated by static estimation: 4643.
MINIMAX estimate: -1010.
  
-------- Alpha-Beta Pruning --------
Board Position: BBWxWxWBBxWxWWBWWBxBB.
Positions evaluated by static estimation: 360.
MINIMAX estimate: -1010.
</pre>

## 4. Improved MiniMax Algorithm
### Opening Phase
- The static estimation function is tweaked to form a potential double mill at an intersection. The basic MiniMax algorithm for Black player does not consider such scenarios at the intersection and places its pieces in the ascending order.
The formation of a potential mill is highlighted by <b>[ ]</b> in both boards.
<pre>
╰─ python3 MiniMaxOpeningImproved.py board1.txt board2.txt 2 --print_board
Input Board:
x--------x--------x
|        |        |
|  W----<b>[x]</b>----x  |
|  |     |     |  |
|  |  x--W--x  |  |
|  |  |     |  |  |
x--x--x     x--x--x
|  |  |     |  |  |
|  |  x-----x  |  |
|  |           |  |
|  x-----------x  |
|                 |
B-----------------B
Output Board:
x--------x--------x
|        |        |
|  W----<b>[W]</b>----x  |
|  |     |     |  |
|  |  x--W--x  |  |
|  |  |     |  |  |
x--x--x     x--x--x
|  |  |     |  |  |
|  |  x-----x  |  |
|  |           |  |
|  x-----------x  |
|                 |
B-----------------B
Board Position: BBxxxxxxxxxxxWxWWxxxx.
Positions evaluated by static estimation: 272.
MINIMAX estimate: 3.
</pre>