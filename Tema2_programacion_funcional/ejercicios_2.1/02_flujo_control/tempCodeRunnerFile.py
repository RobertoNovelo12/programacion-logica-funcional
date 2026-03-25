# Ejercicio 2: Intercambio de posiciones
# Intercambia la primera y la última posición utilizando solo asignación por índice.
numeros = [10, 20, 30, 40, 50]
# Usamos una variable temporal o la sintaxis de empaquetado de Python
numeros[0], numeros[-1] = numeros[-1], numeros[0]
print("Ejercicio 2:", numeros)