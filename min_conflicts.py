import random
import matplotlib.pyplot as plt
import numpy as np
import time

#Inicializa un tablero aleatorio y ejecuta el bucle del algoritmo Min-Conflicts para encontrar una solución donde ninguna reina se ataque.
def solve_nqueens_min_conflicts(n, max_iterations=5000):
    if n <= 3 and n != 1:
        return None
    board = []
    for _ in range(n):
        fila_aleatoria = random.randint(0, n - 1)
        board.append(fila_aleatoria)

    
    #Calcula cuántos ataques tendría una reina en una posición específica verificando la misma fila y las diagonales.
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

    #Identifica qué columnas tienen reinas en conflicto actualmente y selecciona una al azar para intentar moverla; devuelve -1 si no hay conflictos (solución encontrada).
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

#Transforma la lista numérica (donde el índice es columna y el valor es fila) en una representación visual de cadenas con puntos y 'Q'.
def format_board(board, n):
    formatted_board = []
    for row_index in board:
        row_string = '.' * row_index + 'Q' + '.' * (n - 1 - row_index)
        formatted_board.append(row_string)
    return formatted_board







#Transforma la representación visual de cadenas de puntos y 'Q' en un tablero con '♛'
def visualizar_solucion_nqueens(solucion_formateada):
    if not solucion_formateada:
        print("No se proporcionó una solución válida para graficar.")
        return

    n = len(solucion_formateada)
    
    #Crea el tablero
    tablero = np.zeros((n, n))
    tablero[1::2, ::2] = 1
    tablero[::2, 1::2] = 1

    #Ajusta el tamaño del tablero
    figsize_val = min(10, n) 
    fig, ax = plt.subplots(figsize=(figsize_val, figsize_val))
    
    #Dibuja el fondo
    ax.imshow(tablero, cmap='gray_r', interpolation='nearest', origin='upper', extent=[0, n, n, 0])

    #Dibuja las Reinas
    simbolo_reina = '♛' 
    
    fsize = max(5, 500 // n) 
    
    for fila, valor_fila in enumerate(solucion_formateada):
        columna = valor_fila.find('Q')
        if columna != -1:
            ax.text(columna + 0.5, fila + 0.5, simbolo_reina, fontsize=fsize, ha='center', va='center', color='gold', fontweight='bold')


    ax.set_title(f"Solución para N={n}", fontsize=14)
    
    if n > 20:
        ax.axis('off')
    else:
        ax.set_xticks(np.arange(n))
        ax.set_yticks(np.arange(n))
        ax.tick_params(top=True, bottom=False, labeltop=True, labelbottom=False)

    plt.tight_layout()
    plt.show()





inicio1=time.perf_counter()
N = 500
solution = solve_nqueens_min_conflicts(N)
fin1=time.perf_counter()
inicio2=time.perf_counter()
if solution:
    print(f"Tablero de la Solución para N={N} en {fin1-inicio1} segundos:")
    for row in solution:
        print(row)
    visualizar_solucion_nqueens(solution)
    fin2=time.perf_counter()
    print(f"El tablero tardó {fin2-inicio2} segundos en generarse")
else:
    print(f"Fallo al encontrar solución para N = {N} dentro del límite de iteraciones, tardó {fin1-inicio1} segundos.")


Nn=[100,150,200,300,400,500,1000]
T=[0.6,1.24,2.49,6.86,15.34,26.78,188]
It=[162,148,188,290,366,404,682]
