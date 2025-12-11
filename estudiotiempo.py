


###BACKTRACKING PARA n=5
n = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 19, 20, 21, 22, 23, 24, 25, 26, 27]

iteraciones = [
    115, 894, 539, 2008, 1395, 5420, 6391, 10080, 19253, 
    460340, 109890, 125256, 385567, 5158600, 692265, 
    42397564, 2115908, 12703200, 2823075, 28781818, 15038433
]




segundos = [
    8.14e-5, 0.0003, 0.000202, 0.000795, 0.0005, 0.0023, 0.0303, 0.00505, 0.0105, 
    0.025, 0.061, 0.074, 0.24, 3.58, 0.47, 
    31.54, 1.56, 9.74, 2.28, 24.36, 21.52
]

# --- GRAFICA 1: Iteraciones ---
plt.figure(figsize=(10, 6))
plt.plot(n, iteraciones, color='blue')
plt.scatter(n, iteraciones, color='blue')
plt.yscale('log') 
plt.title("Iteraciones en función de las reinas")
plt.xlabel("N")
plt.ylabel("Iteraciones")

plt.grid(True, which="both", ls="--", alpha=0.5)
plt.show()

# GRAFICA 2: Segundos 
plt.figure(figsize=(10, 6))
plt.plot(n, segundos, color='crimson')
plt.scatter(n,segundos, color"crimson")
plt.yscale('log') 
plt.title("Tiempo en función de las reinas")
plt.xlabel("N")
plt.ylabel("Segundos")
plt.grid(True, which="both", ls="--", alpha=0.5)


plt.legend()
plt.show()


###PARA MIND CONFLICTS
n=[5,10,15,20,22,25,28,30,50,100,150,200,300,400,500,1000]
segundos=[0.00069,0.0046,0.003,0.0267,0.0312,0.0081,0.0447,0.018,0.038,0.6,1.24,2.49,6.86,15.34,26.78,188]
iteraciones=[7,200,58,108,156,63,75,100,74,162,148,188,290,366,404,682]
# GRAFICA 2: iteraciones
plt.figure(figsize=(10, 6))
plt.plot(n, iteraciones, color='blue')
plt.scatter(n, iteraciones, color='blue')
plt.yscale('log') 
plt.title("Iteraciones en función de las reinas")
plt.xlabel("N")
plt.ylabel("Iteraciones")

plt.grid(True, which="both", ls="--", alpha=0.5)
plt.show()

# GRAFICA 2: Segundos 
plt.figure(figsize=(10, 6))
plt.plot(n, segundos, color='crimson')
plt.scatter(n,segundos, color"crimson")
plt.yscale('log') 
plt.title("Tiempo en función de las reinas")
plt.xlabel("N")
plt.ylabel("Segundos")
plt.grid(True, which="both", ls="--", alpha=0.5)


plt.legend()
plt.show()


###BACKTRACKING VS MINCONFLICTS


N=[
   5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29
]


iteraciones1 = [
    30, 70, 250, 400, 250, 1000, 700, 4000, 20000, 40000, 150000, 100000, 800000, 50000, 50000,
    400000, 30000000, 40000000, 10000000, 4000000, 1200000, 11000000, 12000000, 90000000, 50000000
]
tiempo1 = [
    2e-5, 8e-5, 3e-5, 3e-4, 1e-4, 4e-4, 4e-4, 2e-3, 9e-3, 1e-2, 8e-2, 4e-2, 4e-1, 2e-2, 2.0,
    4.0, 40.0, 20.0, 7.0, 1.0, 8.0, 10.0, 10.0, 80.0, 50.0
]

n=[5,10,15,20,22,25,28,30,50]
segundos=[0.00069,0.0046,0.003,0.0267,0.0312,0.0081,0.0447,0.018,0.038,]
iteraciones=[7,200,58,108,156,63,75,100,74]
# GRAFICA 2: iteraciones
plt.figure(figsize=(10, 6))
plt.plot(n, iteraciones, color='red',label="minconflicts")
plt.scatter(n, iteraciones, color='red')
plt.plot(N, iteraciones1, color='green',label="backtracking")
plt.scatter(N, iteraciones1, color='green')
plt.yscale('log') 
plt.title("Iteraciones en función de las reinas")
plt.xlabel("N")
plt.ylabel("Iteraciones")

plt.grid(True, which="both", ls="--", alpha=0.5)

plt.legend()
plt.show()


# GRAFICA 2: Segundos 
plt.figure(figsize=(10, 6))
plt.plot(n, segundos, color='red',label="minconflicts")
plt.scatter(n,segundos, color='red')
plt.plot(N,tiempo1, color='green',label="backtracking")
plt.scatter(N, tiempo1, color='green')
plt.yscale('log') 
plt.title("Tiempo en función de las reinas")
plt.xlabel("N")
plt.ylabel("Segundos")
plt.grid(True, which="both", ls="--", alpha=0.5)


plt.legend()
plt.show()


