# 8 Queen Problem using Backtracking

N = 8

# Board
board = [[0 for i in range(N)] for j in range(N)]


# Check whether a queen can be placed
def is_safe(row, col):

    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i = i - 1
        j = j - 1

    # Check upper-right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i = i - 1
        j = j + 1

    return True


# Function to solve the problem
def solve(row):

    # All queens are placed
    if row == N:
        return True

    # Try every column
    for col in range(N):

        if is_safe(row, col):

            # Place queen
            board[row][col] = 1

            # Move to next row
            if solve(row + 1):
                return True

            # Remove queen if solution is not possible
            board[row][col] = 0

    return False


# Print the board
def print_board():

    for i in range(N):
        for j in range(N):

            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")

        print()


# Main program
if solve(0):
    print("Solution for 8 Queens:")
    print_board()
else:
    print("No solution exists.")
