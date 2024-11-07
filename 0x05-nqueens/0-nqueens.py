#!/usr/bin/python3
import sys

def is_valid(board, row, col):
    # Check column and diagonals for conflicts
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(N):
    def backtrack(row, board):
        if row == N:
            # Add the solution to the results
            solution = [[i, board[i]] for i in range(N)]
            results.append(solution)
        else:
            for col in range(N):
                if is_valid(board, row, col):
                    board[row] = col
                    backtrack(row + 1, board)
                    board[row] = -1

    results = []
    board = [-1] * N
    backtrack(0, board)
    return results

def main():
    # Check the argument count
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Validate N as an integer
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Ensure N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Find and print all solutions
    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
