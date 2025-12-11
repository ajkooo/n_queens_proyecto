"""
Programa principal
"""
import backtracking as
import bits
import min_conflicts
import matplotlib.pyplot as plt

N = int(input("Bienvienido al juego de las N-Reinas; introduce, a contiuacón, el tamaño del tablero"))

if N<=0:
    print("Por favor, introduce un tamaño de tablero positivo")
    
if N == 1:
    print("La única solución posible es:")

if N == 2 or N==3: 
    print("La dimensión del tablero ha de ser distinta de 2 o 3")

if N <= 20:
    bactracking

else:
    minconflicts(N, ):


    

