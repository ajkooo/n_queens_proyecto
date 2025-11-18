import numpy as np

n=4
def sepuede(tablero,filas,columnas):

    for i in range(filas):
        #Para comprobar si están en la misma columna
        if tablero[i]==columnas:
            #No se puede colocar reina
            return False
        #Para comprobar si estan en la misma diagonal(ponemos valor absoluto porque si ponemos la diagonal izquierda en uno sale 1 y otro -1)
        elif abs(tablero[i]-columnas)==abs(i-filas):
            return  False
        else:
            #Se coloca la reina
            return True
def probarfila(tablero,filas,n):
    #Vamos a recorrer las columnas para ver si se puede meter una reina 
    for columnas in range(n):
        print("xd")

