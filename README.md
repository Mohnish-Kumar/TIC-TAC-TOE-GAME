# Tic Tac Toe Game

This is a simple command-line implementation of the classic Tic Tac Toe game in Python. Two players take turns marking X and O on a 3x3 grid until one of them wins or the grid is filled, resulting in a draw.

## How to Play

1. Run the script using a Python interpreter.

2. Players will be prompted to enter their names (Player 1 and Player 2).

3. The game board is displayed with numbered positions as follows:

   ```
    7 | 8 | 9 
   ---|---|---
    4 | 5 | 6 
   ---|---|---
    1 | 2 | 3 
   ```

4. Players take turns entering the position number where they want to place their symbol (X for Player 1 and O for Player 2).

5. The game continues until one player wins or the game ends in a draw.

6. If a player wins, the game displays the winner's name.

## Functions

1. `sum(a, b, c)`: Returns the sum of three values `a`, `b`, and `c`.

2. `printBoard(xState, zState)`: Prints the current game board with X and O positions based on `xState` and `zState` lists.

3. `checkWin(xState, zState, player1, player2)`: Checks for a winning condition and returns the winner's name or -1 if no one has won yet.

## Note

This implementation is a simple text-based version of Tic Tac Toe, and the primary purpose is to demonstrate basic programming concepts and logic. More complex games and applications can be built using Python and various libraries.

Enjoy playing Tic Tac Toe! 🎲
