# Jorge Roberto Novelo Poot - 8B
###
# 03 - Listas
# Secuencias mutables de elementos.
# Pueden contener elementos de diferentes tipos.
###

from os import system
if system("clear") != 0: system("cls")

# Creación de listas
print("\nCrear listas")
lista1 = [1, 2, 3, 4, 5] # lista de enteros
lista2 = ["manzanas", "peras", "plátanos"] # lista de cadenas
lista3 = [1, "hola", 3.14, True] # lista de tipos mixtos

lista_vacia = []
lista_de_listas = [[1, 2], ['calcetín', 4]]
matrix = [[1, 2], [2, 3], [4, 5]]

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)
print(matrix)

# Acceso a elementos por índice
print("\nAcceso a elementos por índice")
print(lista2[0]) # manzanas
print(lista2[1]) # peras
print(lista2[-1]) # plátanos
print(lista2[-2]) # peras

print(lista_de_listas[1][0])

# Slicing (rebanado) de listas
lista1 = [1, 2, 3, 4, 5]
print(lista1[1:4]) # [2, 3, 4]
print(lista1[:3]) # [1, 2, 3]
print(lista1[3:]) # [4, 5]
print(lista1[:]) # [1, 2, 3, 4, 5]

# El tercer parámetro es el paso (step)
lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(lista1[::2]) # para devolver índices pares
print(lista1[::-1]) # para devolver índices inversos

# Modificar una lista
lista1[0] = 20
print(lista1)

# Añadir elementos a una lista
lista1 = [1, 2, 3]

# forma larga y menos eficiente
lista1 = lista1 + [4, 5, 6]
print(lista1)

# forma corta y más eficiente
lista1 += [7, 8, 9]
print(lista1)

# Recuperar longitud de una lista
print("Longitud de la lista", len(lista1))

###
# EJERCICIOS
###

# Ejercicio 1: El mensaje secreto
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".
mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
secreto = mensaje[7:]
print("Ejercicio 1:", secreto)


# Ejercicio 2: Intercambio de posiciones
# Intercambia la primera y la última posición utilizando solo asignación por índice.
numeros = [10, 20, 30, 40, 50]
numeros[0], numeros[-1] = numeros[-1], numeros[0]
print("Ejercicio 2:", numeros)


# Ejercicio 3: El sándwich de listas
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo.
pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]

sandwich = pan + ingredientes + pan_abajo
print("Ejercicio 3:", sandwich)


# Ejercicio 4: Duplicando la lista
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
lista = [1, 2, 3]
lista_duplicada = lista + lista
print("Ejercicio 4:", lista_duplicada)


# Ejercicio 5: Extrayendo el centro
# Extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
lista_impar = [10, 20, 30, 40, 50]
centro_index = len(lista_impar) // 2
centro = lista_impar[centro_index : centro_index + 1]
print("Ejercicio 5: El centro es", centro)


# Ejercicio 6: Reversa parcial
# Invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
lista_par = [1, 2, 3, 4, 5, 6]
mitad = len(lista_par) // 2
resultado = lista_par[:mitad][::-1] + lista_par[mitad:]
print("Ejercicio 6:", resultado)