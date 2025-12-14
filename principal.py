import backtracking
import min_conflicts
import matplotlib1
import time

# Tabla de soluciones totales conocidas para validación rápida (OEIS A000170)
SOLUCIONES_CONOCIDAS = {
    1: 1, 2: 0, 3: 0, 4: 2, 5: 10, 6: 4, 7: 40, 8: 92, 
    9: 352, 10: 724, 11: 2680, 12: 14200, 13: 73712, 14: 365596, 15: 2279184
}

def main():
    print("=== PROGRAMA PRINCIPAL N-REINAS ===")
    
    while True:
        try:
            entrada = input("\nIntroduzca el tamaño del tablero (N) o 's' para salir: ")
            if entrada.lower() == 's':
                break
            N = int(entrada)
        except ValueError:
            print("Por favor, introduce un número entero válido.")
            continue

        if N <= 0:
            print("Por favor, introduce un tamaño positivo.")
            continue
        
        if N == 1:
            print("Solución trivial.")
            matplotlib1.dibujar_tablero([0], 1, 1)
            continue

        if N == 2 or N == 3: 
            print("La dimensión del tablero ha de ser distinta de 2 o 3 (sin solución).")
            continue

        # --- NUEVA LÓGICA DE SELECCIÓN ---
        print(f"\nOpciones para N={N}:")
        if N > 20:
            print("(!) Recomendación: Para N > 20 es más eficiente: Min-conflicts.")
        
        modo = input("Elige algoritmo: 'b': Backtracking, 'm': Min-conflicts o 'c': Comparativa: ").lower()
        
        soluciones = []
        
        # --- OPCIÓN C: COMPARATIVA ---
        if modo == 'c':
            print(f"\n--- Comparativa de tiempos (N={N}) para 1 solución ---")
            
            # 1. Medir Backtracking
            start_b = time.perf_counter()
            sol_b = backtracking.soluciones_reinas(N, limite_soluciones=1)
            end_b = time.perf_counter()
            tiempo_b = end_b - start_b
            
            if sol_b:
                print(f"Backtracking:   {tiempo_b:.6f} segundos.")
            else:
                print(f"Backtracking:   Tiempo límite excedido o sin solución.")

            # 2. Medir Min-Conflicts
            start_m = time.perf_counter()
            iters = 1000 if N > 50 else 5000 
            sol_m = min_conflicts.solve_nqueens_min_conflicts(N, max_iterations=iters)
            end_m = time.perf_counter()
            tiempo_m = end_m - start_m

            if sol_m:
                print(f"Min-Conflicts:  {tiempo_m:.6f} segundos.")
            else:
                print(f"Min-Conflicts:  No encontró solución en el límite de iteraciones.")

            if sol_b and sol_m:
                ganador = "Backtracking" if tiempo_b < tiempo_m else "Min-Conflicts"
                print(f"--> Más rápido: {ganador}")
            continue

        # --- OPCIÓN B: BACKTRACKING (MODIFICADO) ---
        elif modo == 'b':
            opcion_cant = input("¿Cuántas soluciones? Introduzca un número o 't' para todas: ").lower()
            
            limite = 1
            
            if opcion_cant == 't':
                limite = float('inf') # Infinito para buscar todas
                print(f"Calculando TODAS las soluciones posibles para N={N}...")
            else:
                try:
                    limite = int(opcion_cant)
                    # VALIDACIÓN DE LÍMITE (Raise ValueError si excedemos las posibles)
                    if N in SOLUCIONES_CONOCIDAS:
                        max_posible = SOLUCIONES_CONOCIDAS[N]
                        if limite > max_posible:
                            # Lanzamos el error explícitamente como pediste
                            raise ValueError(f"Estás pidiendo {limite} soluciones, pero para N={N} solo existen {max_posible}.")
                            
                except ValueError as e:
                    print(f"\n[ERROR]: {e}")
                    # Volvemos al inicio del bucle principal
                    continue 

            print(f"Ejecutando Backtracking...")
            start = time.time()
            soluciones = backtracking.soluciones_reinas(N, limite_soluciones=limite)
            end = time.time()
            
            cant_encontradas = len(soluciones)
            if soluciones:
                print(f"Se encontraron {cant_encontradas} solución(es) en {end - start:.4f} s.")
                
                # Bucle interactivo paso a paso
                for i, sol in enumerate(soluciones):
                    matplotlib1.dibujar_tablero(sol, i + 1, cant_encontradas)
                    
                    if i < cant_encontradas - 1:
                        seguir = input("¿Mostrar siguiente solución? (s/n): ").lower()
                        if seguir != 's':
                            break
            else:
                print("No se encontraron soluciones.")

        # --- OPCIÓN M: MIN-CONFLICTS ---
        elif modo == 'm':
            print(f"Usando Min-Conflicts para N={N}...")
            start = time.time()
            iters = 10000 if N > 100 else 5000
            una_solucion = min_conflicts.solve_nqueens_min_conflicts(N, max_iterations=iters)
            end = time.time()
            
            if una_solucion:
                print(f"¡Solución encontrada en {end - start:.4f} s!")
                matplotlib1.dibujar_tablero(una_solucion, 1, 1)
            else:
                print("No se pudo encontrar una solución dentro del límite de iteraciones.")

        else:
            print("Opción no reconocida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
