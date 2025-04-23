import random

def is_valid(board):
    for i in range(8):
        for j in range(i + 1, 8):
            if abs(i - j) == abs(board[i] - board[j]):
                return False
    return True

def random_queens():
    while True:
        cols = list(range(8))
        random.shuffle(cols)
        if is_valid(cols):
            return cols

print(random_queens())