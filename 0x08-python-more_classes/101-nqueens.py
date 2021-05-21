#!/usr/bin/python3
def is_safe(board, row, column):

    for c in range(column):
        if board[c] is row or abs(board[c] - row) is abs(c - column):
            return False

    return True


def check_board(board, column, n):

    if column is n:
        print(str([[c, board[c]] for c in range(n)]))
        return

    for row in range(n):
        if is_safe(board, row, column):
            board[column] = row
            check_board(board, column + 1, n)

if __name__ == "__main__":
    import sys

    n = 0

    try:
        n = int(sys.argv[1])
    except:
        print("N must be a number")
        sys.exit(1)

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    board = [0 for row in range(n)]

    check_board(board, 0, n)
