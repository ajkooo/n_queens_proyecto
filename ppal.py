import sys

# Constante para el tamaño del tablero
N = 8

def imprimir_solucion(tablero):
    """
    Función auxiliar para imprimir el tablero de forma visual.
    """
    for fila in range(N):
        linea = ""
        for col in range(N):
            if tablero[col] == fila:
                linea += "Q "
            else:
                linea += ". "
        print(linea)
    print("\n")

def es_seguro(tablero, fila, col):
    """
    Verifica si es seguro colocar una reina en tablero[col] = fila.
    Solo necesitamos comprobar las columnas a la izquierda de 'col',
    ya que las de la derecha aún no tienen reinas.
    """
    for i in range(col):
        # 1. Comprobar la misma fila
        if tablero[i] == fila:
            return False
        
        # 2. Comprobar la diagonal
        # abs(fila_previa - fila_actual) == abs(col_previa - col_actual)
        if abs(tablero[i] - fila) == abs(i - col):
            return False
            
    # Si no hay conflictos, es seguro
    return True

def resolver_reinas_util(tablero, col, soluciones):
    """
    Función recursiva (backtracking) para resolver el problema.
    """
    # CASO BASE: Si hemos llegado más allá de la última columna (col == N),
    # significa que hemos colocado las N reinas con éxito.
    if col == N:
        # Guardamos una copia de la solución
        soluciones.append(list(tablero))
        return

    # CASO RECURSIVO: Intentar colocar una reina en cada fila de la columna actual
    for fila in range(N):
        
        # Comprobamos si la posición (fila, col) es segura
        if es_seguro(tablero, fila, col):
            
            # 1. Colocar la reina
            tablero[col] = fila
            
            # 2. Llamada recursiva para la siguiente columna
            resolver_reinas_util(tablero, col + 1, soluciones)
            
            # 3. Backtracking: Quitamos la reina (no es necesario en este
            #    diseño, ya que 'tablero[col] = fila' se sobrescribirá
            #    en la siguiente iteración del bucle, pero es
            #    conceptual).

def resolver_n_reinas():
    """
    Función principal que inicializa y lanza la solución.
    """
    soluciones = []
    
    # Usamos un array de 1D. El índice 'col' representa la columna,
    # y el valor 'tablero[col]' representa la fila donde está la reina.
    # Inicializamos con -1 (ninguna reina colocada).
    tablero = [-1] * N
    
    # Empezamos por la columna 0
    resolver_reinas_util(tablero, 0, soluciones)
    
    return soluciones

# --- Ejecución Principal ---
if __name__ == "__main__":
    soluciones_encontradas = resolver_n_reinas()
    
    print(f"Problema de las {N} reinas")
    print(f"Se encontraron {len(soluciones_encontradas)} soluciones únicas.\n")
    
    # Imprimir las primeras 3 soluciones para no saturar la consola
    for i, sol in enumerate(soluciones_encontradas[:3]):
        print(f"--- Solución {i + 1} ---")
        imprimir_solucion(sol)
        
    print(f"Se imprimieron 3 de {len(soluciones_encontradas)} soluciones.")
