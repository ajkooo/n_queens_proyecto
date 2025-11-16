def is_valid(row, col, queens):
    for r in range(row):
        if col == queens[r]: return False
        elif abs(col - queens[r]) == abs(row - r): return False
    return True
"""
is_valid se asegura si es posible colocar una reina en (row, col), para que no choque con las reinas ya puestas
o no se coman entre ellas. Por cada fila (0, n), el bucle comprueba si el valor de la columna coincide con el
valor de la columna en la que está situada una reina. No hace falta que comprobemos las filas porque ya estamos comprobando
una fila diferente cada vez. 
"""
    

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
