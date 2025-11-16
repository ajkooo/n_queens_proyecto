def is_valid(row, col, queens):
    for r in range(row):
        if col == queens[r]: return False
        elif abs(col - queens[r]) == abs(row - r): return False
    return True
    

def place_queen(row, queens, n):
    if row == n:
        print(queens)
        return 1
    else:
        total_solutions = 0
        for col in range(n):
            if is_valid(row, col, queens):
                queens[row] = col
                total_solutions += place_queen(row+1, queens, n)
        return total_solutions



def n_queens(n):
    queens = [' ']*n
    row = 0
    return place_queen(row, queens, n)
