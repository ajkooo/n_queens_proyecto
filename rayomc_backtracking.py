def es_seguro(tablero, fila, col):
    for i in range(fila):  
        if tablero[i] == col:
            return False                     
        if abs(tablero[i] - col) == fila - i:
            return False                     
    return True

def resolver_n_reinas_verbose(n):
    tablero = [-1] * n
    soluciones = []

    def backtracking(fila):
        if fila == n:
            soluciones.append(tablero.copy())
            return

        for col in range(n):

            seguro = es_seguro(tablero, fila, col)

            if not seguro:
                continue

            tablero[fila] = col
            backtracking(fila + 1)

            tablero[fila] = -1

    backtracking(0)
    return soluciones

def imprimir_tablero(sol):
    """Imprime una solución como tablero visual."""
    n = len(sol)
    for fila in range(n):
        row = "".join("Q " if col == sol[fila] else ". " for col in range(n))
        print(row)
    print()

n=(int(input("Introduzca el numero de reinas: ")))
soluciones = resolver_n_reinas_verbose(n)
print(f"\nTotal soluciones encontradas: {len(soluciones)}\n")
for s in soluciones:
    imprimir_tablero(s)
