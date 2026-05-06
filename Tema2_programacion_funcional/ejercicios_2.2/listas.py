numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

doble =[] #lista vacia

for n in numeros:
    doble.append(n*2)

print(doble)

cuadrados = [num ** 2 for num in numeros]
lista_cuadruple=list(map(lambda x: x * 4, numeros))
print(lista_cuadruple)

cubo = [elemento ** 3 for elemento in numeros]

cadena = ["hola "+"que hace" for _ in range(3)]

saludos = ["hola" for _ in range(5)]
saludos2 = ["que hace" for _ in range(3)]