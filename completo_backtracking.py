def is_valid(row, col, queens):
    for r in range(row):
        if col == queens[r]: return False
        elif abs(col - queens[r]) == abs(row - r): return False
    return True
"""
is_valid se asegura si es posible colocar una reina en (row, col), para que no choque con las reinas ya puestas
o no se coman entre ellas. Por cada fila (0, n), el bucle comprueba si el valor de la columna coincide con el
valor de la columna en la que está situada una reina. No hace falta que comprobemos las filas porque el algoritmo solo
coloca una reina por fila a la vez. También deberemos comprobar las diagonales (con reinas dispuestas a 45º unas de otras), en cuyo caso,
la diferencia absoluta entre las filas es igual a la diferencia absoluta entre las columnas (pendiente).
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
"""
place_queen coloca una reina en cada columna posible de la fila. Si row == n; quiere decir que hemos avanzado más allá de la última
fila (n-1): la configuración actual de queens es una solción completa. Si no, evaluara las columnas en la fila prefijada del bucle (la 0),
hasta colocarla en el primer hueco posible. Cuando esto occure, le sumamos a la fila +1 para avanzar a la siguiende fila (hacemos llamada a la
función desde un nivel mas bajo). El programa vuelve a evaluar en la fila 1 las posibles soluciones, para pasar luego a la 2. Si al llegar a una
nueva fila no puede colocar una reina (is_valid), comienza el proceso de backtracking y se cambia la reina de la fila anterior (al no haber cumplido 
is_valudm row+1 se queda prefijada).
Funcionamiento del contador: Se le añade 1 solucion si 

"""

def n_queens(n):
    queens = [' ']*n
    row = 0
    return place_queen(row, queens, n)
