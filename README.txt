First of all, we need to provide input and corresponding size for the matrix.
1. Size of the matrix: change the values of COLS and ROWS in config.py
2. Generate input: obtain randomly generated input by running gen_input(n) funtion in utilities.py where n is the number of moves that we would like to move the 0-tile to obtain the input from the goal state.

Once we have the input, run the algorithms as follows:
- DFS: python puzzleDFS-ite.py
- BFS-h1: python puzzleBFS-h1.py
- BFS-h2: python puzzleBFS-h2.py
- AS-h1: python puzzleAS-h1.py
- AS-h2: python puzzleAs-h2.py

The output for each algorithm can be found in the corresponding .txt file (ie. puzzleDFS-ite.txt for puzzleDFS-ite.py)