import random

# Inicializa un tablero aleatorio y ejecuta el bucle del algoritmo Min-Conflicts
def solve_nqueens_min_conflicts(n, max_iterations=5000):
    if n <= 3 and n != 1:
        return None
        
    # board[col] = row (El índice es la columna, el valor la fila)
    board = []
    for _ in range(n):
        fila_aleatoria = random.randint(0, n - 1)
        board.append(fila_aleatoria)

    # Calcula cuántos ataques tendría una reina en una posición específica
    def count_conflicts(test_board, col, row):
        conflicts = 0
        for c in range(n):
            if c == col:
                continue
            r = test_board[c]
            if r == row:
                conflicts = conflicts + 1
            elif abs(r - row) == abs(c - col):
                conflicts = conflicts + 1
        return conflicts

    # Identifica qué columnas tienen reinas en conflicto
    def get_conflicted_column(current_board):
        conflicted_cols = []
        for c in range(n):
            numero_de_conflictos = count_conflicts(current_board, c, current_board[c])
            if numero_de_conflictos > 0:
                conflicted_cols.append(c)
        
        if not conflicted_cols:
            return -1 
        
        return random.choice(conflicted_cols)

    for i in range(max_iterations):
        col = get_conflicted_column(board)
        if col == -1:
            # Solución encontrada
            return transponer_solucion(board, n)
        
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

    return None

def transponer_solucion(board_cols, n):
    """
    Convierte el formato de MinConflicts (Indice=Col, Valor=Fila)
    al formato de Backtracking/Visualizador (Indice=Fila, Valor=Col).
    """
    board_rows = [-1] * n
    for col, row in enumerate(board_cols):
        board_rows[row] = col
    return board_rows
