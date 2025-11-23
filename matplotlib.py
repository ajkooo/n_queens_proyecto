import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
import numpy as np

# --- LÓGICA DEL ALGORITMO ---

def is_valid(row, col, queens):
    """Verifica si es seguro colocar una reina en la posición (row, col)."""
    for r in range(row):
        if col == queens[r]: 
            return False
        elif abs(col - queens[r]) == abs(row - r): 
            return False
    return True

def solve_n_queens_multiple(n, limite_soluciones=5):
    """
    Encuentra hasta 'limite_soluciones' distintas para N reinas usando Backtracking.
    Devuelve una lista de soluciones.
    """
    queens = [-1] * n
    solutions = []
    
    def place_queen(row):
        # Si ya tenemos suficientes soluciones, paramos la búsqueda para no saturar
        if len(solutions) >= limite_soluciones:
            return

        if row == n:
            solutions.append(list(queens))
            return
        
        for col in range(n):
            if is_valid(row, col, queens):
                queens[row] = col
                place_queen(row + 1)
                # Backtracking: quitamos la reina para probar la siguiente columna
                queens[row] = -1 

    place_queen(0)
    return solutions

# --- VISUALIZACIÓN GRÁFICA ---

def dibujar_tablero(solucion, indice, total_encontradas):
    n = len(solucion)
    
    # 1. Crear tablero ajedrez
    tablero = np.zeros((n, n))
    tablero[1::2, ::2] = 1
    tablero[::2, 1::2] = 1

    # 2. Configurar la figura
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.imshow(tablero, cmap='binary', origin='upper', alpha=1)

    # 3. Colocar Reinas
    for fila, columna in enumerate(solucion):
        txt = ax.text(columna, fila, '♛', fontsize=30 if n < 10 else 15, # Ajustar tamaño si N es grande
                      ha='center', va='center', color='gold', fontweight='bold')
        txt.set_path_effects([path_effects.withStroke(linewidth=2, foreground='black')])

    # 4. Ajustes estéticos
    ax.set_xticks(np.arange(n))
    ax.set_yticks(np.arange(n))
    ax.set_xticklabels(np.arange(n))
    ax.set_yticklabels(np.arange(n))
    
    ax.set_title(f"Solución {indice} de {total_encontradas} encontradas\nVector: {solucion}", fontsize=12)
    ax.tick_params(length=0)

    print(f"--> Mostrando Solución #{indice}. Cierra la ventana para continuar.")
    plt.show(block=True)

# --- BLOQUE PRINCIPAL ---

if __name__ == "__main__":
    while True:
        try:
            entrada = input("\nIntroduzca el número de reinas (N): ")
            if not entrada.strip(): continue # Si está vacío, pide otra vez
            N = int(entrada)
            break
        except ValueError:
            print("Por favor, introduce un número entero válido.")

    # LÓGICA DE CONTROL SEGÚN TU PETICIÓN
    soluciones = []

    if N == 1:
        print("\nCaso N=1: Solución trivial.")
        soluciones = [[0]]

    elif N == 2 or N == 3:
        print(f"\n[ERROR] No existen soluciones para N={N} (Problema imposible).")
        # No generamos soluciones, la lista se queda vacía

    elif 3 < N <= 20:
        print(f"\nUsando Backtracking para N={N}...")
        # Buscamos hasta 10 soluciones para que puedas ver varias
        # Si quieres ver TODAS (pueden ser muchas), cambia el límite a un número muy alto
        soluciones = solve_n_queens_multiple(N, limite_soluciones=10)
        if not soluciones:
             print(f"No se encontraron soluciones (algo raro pasó para N={N}).")
    
    else:
        print(f"\nN={N} está fuera del rango soportado por este ejemplo (max 20).")

    # VISUALIZACIÓN DE RESULTADOS
    if soluciones:
        print(f"Se han cargado {len(soluciones)} soluciones distintas.")
        
        for i, sol in enumerate(soluciones):
            print(f"Solución {i+1}: {sol}")
            dibujar_tablero(sol, i+1, len(soluciones))
            
            # Preguntar si quiere ver la siguiente (si quedan más)
            if i < len(soluciones) - 1:
                seguir = input("¿Ver la siguiente solución? (s/n): ").lower()
                if seguir == 'n':
                    break
        print("\nFin del programa.")
