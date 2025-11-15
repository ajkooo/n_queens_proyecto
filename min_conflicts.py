import numpy as np
n = 8
Q = np.random.randint(0, n, size=n)
print(Q)

def to_matrix(Q):
    n = len(Q)
    board = np.zeros((n, n), dtype=int)
    for col, fila in enumerate(Q):
        board[fila, col] = 1
    return board

print(to_matrix(Q))
