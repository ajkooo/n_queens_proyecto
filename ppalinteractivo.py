import tkinter as tk
from tkinter import messagebox
import random
import time

# ==========================================
# LÓGICA DEL ALGORITMO 1: BACKTRACKING
# (Para N <= 20: Busca solución exacta)
# ==========================================
def is_valid_backtrack(row, col, queens):
    for r in range(row):
        if col == queens[r]: return False
        elif abs(col - queens[r]) == abs(row - r): return False
    return True

def solve_backtracking_single(n):
    """
    Modificado para devolver la PRIMERA solución encontrada
    en lugar de contar todas las soluciones.
    Retorna: Lista donde índice=fila, valor=columna.
    """
    queens = [-1] * n
    row = 0
    
    # Usamos una pila para simular recursividad y poder detenernos
    # o una función recursiva con retorno booleano.
    # Aquí usaré una función auxiliar recursiva simple.
    
    def place(r):
        if r == n:
            return True
        for c in range(n):
            if is_valid_backtrack(r, c, queens):
                queens[r] = c
                if place(r + 1):
                    return True
                queens[r] = -1 # Backtrack
        return False

    if place(0):
        return queens
    else:
        return None

# ==========================================
# LÓGICA DEL ALGORITMO 2: MIN-CONFLICTS
# (Para N > 20: Heurística rápida)
# ==========================================
def solve_min_conflicts(n, max_iterations=5000):
    # Configuración inicial: una reina por columna en fila aleatoria
    board = [random.randint(0, n - 1) for _ in range(n)] # Índice=Columna, Valor=Fila

    def count_conflicts(current_board, col, row):
        conflicts = 0
        for c in range(n):
            if c == col: continue
            r = current_board[c]
            if r == row: conflicts += 1
            elif abs(r - row) == abs(c - col): conflicts += 1
        return conflicts

    def get_conflicted_column(current_board):
        conflicted_cols = []
        for c in range(n):
            if count_conflicts(current_board, c, current_board[c]) > 0:
                conflicted_cols.append(c)
        if not conflicted_cols: return -1
        return random.choice(conflicted_cols)

    for i in range(max_iterations):
        col = get_conflicted_column(board)
        if col == -1:
            return board # Solución encontrada
        
        # Encontrar la mejor fila para esta columna
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

    return None

# ==========================================
# INTERFAZ GRÁFICA (TKINTER)
# ==========================================
class NQueensApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizador N-Reinas")
        self.root.geometry("700x750")
        self.root.configure(bg="#f0f0f0")

        # --- Panel de Control ---
        control_frame = tk.Frame(root, bg="#e0e0e0", pady=10)
        control_frame.pack(fill="x")

        tk.Label(control_frame, text="Tamaño del tablero (N):", bg="#e0e0e0", font=("Arial", 12)).pack(side="left", padx=10)
        
        self.entry_n = tk.Entry(control_frame, font=("Arial", 12), width=10)
        self.entry_n.insert(0, "8") # Valor por defecto
        self.entry_n.pack(side="left", padx=5)

        self.btn_solve = tk.Button(control_frame, text="🧠 Resolver", command=self.run_solver, 
                                   bg="#4CAF50", fg="white", font=("Arial", 11, "bold"))
        self.btn_solve.pack(side="left", padx=10)

        self.lbl_status = tk.Label(control_frame, text="Listo", bg="#e0e0e0", fg="#333", font=("Arial", 10, "italic"))
        self.lbl_status.pack(side="left", padx=20)

        # --- Área de Dibujo (Canvas) ---
        self.canvas_size = 600
        self.canvas = tk.Canvas(root, width=self.canvas_size, height=self.canvas_size, bg="white", highlightthickness=0)
        self.canvas.pack(pady=20)

    def draw_board(self, n, solution, solution_type):
        """
        Dibuja el tablero y las reinas.
        solution_type: 'backtracking' (idx=fila, val=col) o 'min_conflicts' (idx=col, val=fila)
        """
        self.canvas.delete("all")
        
        # Si N es muy grande, no dibujamos las casillas individuales para no congelar la GUI
        # pero dibujamos las reinas como puntos.
        cell_size = self.canvas_size / n
        draw_grid = True if n <= 50 else False
        
        # 1. Dibujar Grid (Tablero)
        if draw_grid:
            for r in range(n):
                for c in range(n):
                    color = "#DDB88C" if (r + c) % 2 == 0 else "#A66D4F" # Colores estilo madera
                    x1 = c * cell_size
                    y1 = r * cell_size
                    x2 = x1 + cell_size
                    y2 = y1 + cell_size
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

        # 2. Dibujar Reinas
        font_size = int(cell_size * 0.7)
        if font_size < 1: font_size = 1

        for i in range(n):
            # Normalizar coordenadas según el algoritmo usado
            if solution_type == 'backtracking':
                r, c = i, solution[i]
            else: # min_conflicts
                c, r = i, solution[i]

            x1 = c * cell_size
            y1 = r * cell_size
            
            # Dibujo de la reina
            if n <= 50:
                # Usar carácter Unicode de reina para tableros visibles
                center_x = x1 + cell_size / 2
                center_y = y1 + cell_size / 2
                self.canvas.create_text(center_x, center_y, text="♛", fill="black", font=("Arial", font_size))
            else:
                # Para tableros gigantes, dibujar puntos simples
                self.canvas.create_rectangle(x1, y1, x1+cell_size, y1+cell_size, fill="red", outline="")

    def run_solver(self):
        try:
            n = int(self.entry_n.get())
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce un número entero válido.")
            return

        if n == 1:
            self.draw_board(1, [0], 'backtracking')
            self.lbl_status.config(text="Solución trivial encontrada.")
            return
        if n == 2 or n == 3:
            messagebox.showinfo("Sin solución", f"No existe solución matemática para N={n}.")
            return

        self.lbl_status.config(text="Calculando... Espere por favor.")
        self.root.update() # Forzar actualización de la UI antes del cálculo pesado

        start_time = time.perf_counter()
        solution = None
        method = ""

        # Selección automática de algoritmo
        if n <= 20:
            method = "backtracking"
            # Nota: El backtracking devuelve [columna de fila 0, columna de fila 1...]
            solution = solve_backtracking_single(n)
        else:
            method = "min_conflicts"
            # Nota: El min_conflicts devuelve [fila de col 0, fila de col 1...]
            solution = solve_min_conflicts(n)

        end_time = time.perf_counter()
        elapsed = end_time - start_time

        if solution:
            self.lbl_status.config(text=f"Solución encontrada en {elapsed:.4f}s usando {method.capitalize()}.")
            
            # Advertencia para renderizado muy pesado
            if n > 200:
                if not messagebox.askyesno("Tablero Grande", f"N={n} es muy grande. Dibujarlo puede tardar.\n¿Continuar?"):
                    return
            
            self.draw_board(n, solution, method)
        else:
            self.lbl_status.config(text="No se encontró solución (límite alcanzado).")
            messagebox.showwarning("Fallo", "El algoritmo no pudo converger en una solución válida.")

if __name__ == "__main__":
    root = tk.Tk()
    app = NQueensApp(root)
    root.mainloop()
