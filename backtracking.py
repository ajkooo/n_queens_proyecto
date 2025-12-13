import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
import numpy as np

n=4
# --- LÓGICA DEL ALGORITMO ---

def es_valido(fila, col, reinas):
    
    for r in range(fila):
         #Para comprobar si están en la misma columna
        if col == reinas[r]: 
            return False
        #Para comprobar si estan en la misma diagonal
        elif abs(col - reinas[r]) == abs(fila - r): 
            return False
    #Se coloca la reina    
    return True

def soluciones_reinas(n, limite_soluciones=1):
    
    reinas = [-1] * n
    soluciones = []
    
    def colocar_reinas(fila):
        # Si ya tenemos suficientes soluciones, paramos la búsqueda para no saturar
        if len(soluciones) >= limite_soluciones:
            return

        if fila== n:
           #Criterio de parada
            soluciones.append(list(reinas))
            return
        for col in range(n):
            if es_valido(fila, col, reinas):
                #Si es seguro entonces coloca una reina en la fila y columnas dadas
                reinas[fila] = col
                #Ahora coloca la reina para la siguiente fila, hasta o bien encontrar la solución 
                #o darse cuente de que no se puede con las colocaciones que se tenían anteriormente
                colocar_reinas(fila+ 1)
                # Backtracking: quitamos la reina para probar la siguiente columna
                reinas[fila] = -1 
        
#Empieza colocando la reina en la fila 0
    colocar_reinas(0)
    return soluciones

# Protegemos el print para que no salga al importar el módulo
if __name__ == "__main__":
    print(soluciones_reinas(n=8))
