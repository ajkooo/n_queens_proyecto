import random
def solve_nqueens_min_conflicts(n, max_iterations=5000):
    if n <= 3 and n != 1:
        return None
        
    board = [random.randint(0, n - 1) for _ in range(n)]

    
    def count_conflicts(test_board, col, row):
        conflicts = 0
        for c in range(n):
            if c == col:
                continue
            
            r = test_board[c]
            
            if r == row:
                conflicts += 1
                
            elif abs(r - row) == abs(c - col):
                conflicts += 1
                
        return conflicts

    def get_conflicted_column(current_board):
        conflicted_cols = [c for c in range(n) if count_conflicts(current_board, c, current_board[c]) > 0]
        
        if not conflicted_cols:
            return -1 
        
        return random.choice(conflicted_cols)

     for i in range(max_iterations):
        col = get_conflicted_column(board)
        if col == -1:
            print(f"Solución encontrada en {i} iteraciones.")
            return format_board(board, n)
        
        current_row = board[col]
        min_conflicts = float('inf')
        best_rows = [] 

        for r in range(n):
            conflicts = count_conflicts(board, col, r)
            
            if conflicts < min_conflicts:
                min_conflicts = conflicts
                best_rows = [r]
            elif conflicts == min_conflicts:
                best_rows.append(r)
        
        board[col] = random.choice(best_rows)

    print(f"Límite de {max_iterations} iteraciones alcanzado sin solución.")
    return None

def format_board(board, n):
    formatted_board = []
    for row_index in board:
        row_string = '.' * row_index + 'Q' + '.' * (n - 1 - row_index)
        formatted_board.append(row_string)
    return formatted_board

N = 500 
solution = solve_nqueens_min_conflicts(N)
if solution:
    print(f"Tablero de la Solución para N={N}:")
    for row in solution:
        print(row)
else:
    print(f"Fallo al encontrar solución para N = {N} dentro del límite de iteraciones.")
