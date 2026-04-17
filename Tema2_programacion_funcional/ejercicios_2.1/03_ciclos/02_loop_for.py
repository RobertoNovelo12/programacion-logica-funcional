# Jorge Roberto Novelo Poot - 8B
from os import system
if system("clear") != 0: system("cls")

print("\n Bucle for")

frutas = ["manzana", "pera", "mandarina"]

for fruta in frutas:
    print(fruta)

cadena = "estudiante"
for caracter in cadena:
    print(caracter)

frutas = ["manzana", "pera", "mandarina"]
for idx, value in enumerate(frutas):
    print(f"El indice es {idx} y la fruta es {value}")

letras = ["A", "B", "C"]
numeros = [1, 2, 3]


for letra in letras:
    for numero in numeros:
        print(f"{letra}{numero}")

print("\n break")

animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
for idx, animal in enumerate(animales):
    print(animal)
    if animal == "loro":
        print(f"El loro esta escondido en el indice {idx}")

print(animal)

print("\n continue")
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
for idx, animal in enumerate(animales):
    if animal == "loro": continue

    print(animal)



animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
animales_mayus = [animal.upper() for animal in animales]
print(animales_mayus)

pares = [num for num in (1, 2, 3, 4, 5, 6) if num % 2 == 0]
print(pares)


#YO FUNCIONES

print("-------------- EJERCICIOS -----------------")
# EJERICIOS FOR - JORGE ROBERTO NOVELO POOT

# Ejercicio 1: Imprimir números pares

for i in range(2, 21, 2):
    print(i)

# Ejercicio 2: Calcular la media de una lista

numeros = [10, 20, 30, 40, 50]
suma = 0

for n in numeros:
    suma += n

media = suma / len(numeros)
print(f"La media es: {media}")

# Ejercicio 3: Buscar el máximo de una lista

numeros = [15, 5, 25, 10, 20]
maximo = numeros[0]

for n in numeros:
    if n > maximo:
        maximo = n

print(f"El número maximo es: {maximo}")

# Ejercicio 4: Filtrar cadenas por longitud

palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]
filtradas_for = []
for p in palabras:
    if len(p) > 5:
        filtradas_for.append(p)

print(f"Palabras con más de 5 letras: {filtradas_for}")

# Ejercicio 5: Contar palabras que empiezan con una letra

palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]
letra_usuario = input("Introduce una letra: ").lower()
contador = 0

for p in palabras:
    if p[0].lower() == letra_usuario:
        contador += 1

print(f"Hay {contador} palabras que empiezan con la letra '{letra_usuario}'.")