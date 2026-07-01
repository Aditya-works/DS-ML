import numpy as np

board = np.zeros((3, 3), dtype=int)

symbols = {
    0: " ",
    1: "X",
    -1: "O"
}

def print_board():
    print("\nCurrent Board:\n")
    for i in range(3):
        print(" " + " | ".join(symbols[x] for x in board[i]))
        if i < 2:
            print("---+---+---")
    print()

def check_winner(board):
    if 3 in np.sum(board, axis=1):
        return "X"
    if -3 in np.sum(board, axis=1):
        return "O"

    if 3 in np.sum(board, axis=0):
        return "X"
    if -3 in np.sum(board, axis=0):
        return "O"

    if np.trace(board) == 3 or np.trace(np.fliplr(board)) == 3:
        return "X"

    if np.trace(board) == -3 or np.trace(np.fliplr(board)) == -3:
        return "O"

    if not (board == 0).any():
        return "DRAW"

    return None

current = 1

while True:
    print_board()

    player = "X" if current == 1 else "O"
    print(f"Player {player}'s Turn")

    try:
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))
    except ValueError:
        print("Please enter valid numbers.\n")
        continue

    if row < 0 or row > 2 or col < 0 or col > 2:
        print("Invalid position! Enter values between 0 and 2.\n")
        continue

    if board[row][col] != 0:
        print("Cell already occupied! Try again.\n")
        continue

    board[row][col] = current

    result = check_winner(board)

    if result == "X":
        print_board()
        print("Player X Wins!")
        break

    if result == "O":
        print_board()
        print("Player O Wins!")
        break

    if result == "DRAW":
        print_board()
        print("The Match is a Draw!")
        break

    current *= -1