import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
import numpy as np

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
