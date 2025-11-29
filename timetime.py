import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
import numpy as np
import time # <--- 1. ¡NUEVA IMPORTACIÓN!

# --- LÓGICA DEL ALGORITMO ---
# ... (Tu código is_valid y solve_n_queens_multiple sin cambios) ...

def is_valid(row, col, queens):
    # ... (código) ...
    pass

def solve_n_queens_multiple(n, limite_soluciones=5):
    # ... (código) ...
    pass

# --- MEDICIÓN DEL TIEMPO Y EJECUCIÓN ---

N = 8 # Define el tamaño del tablero

# 2. Registrar el tiempo de inicio
start_time = time.time() # <--- 2. ¡NUEVA LÍNEA!

# 3. Ejecutar la función (la parte que quieres medir)
solutions = solve_n_queens_multiple(N, limite_soluciones=5)

# 4. Registrar el tiempo de finalización
end_time = time.time() # <--- 3. ¡NUEVA LÍNEA!

# 5. Calcular la duración y mostrar el resultado
execution_time = end_time - start_time

print(f"Soluciones encontradas: {len(solutions)}")
print(f"Tiempo de ejecución: {execution_time:.4f} segundos") # <--- 4. ¡NUEVA LÍNEA!
