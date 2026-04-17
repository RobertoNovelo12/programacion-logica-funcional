# Jorge Roberto Novelo Poot - 8B
from os import system
if system("clear") != 0: system("cls")


print("\n Bucle while")

contador = 0

while contador <= 5:
    print(contador)
    contador += 1

print("\n Bucle while con break")

contador = 0

while True:
    print(contador)
    contador += 1
    if contador == 5:
        break

print("\n Bucle con continue")

contador = 0

while contador < 10:
    contador += 1

    if contador % 2 == 0:
        continue
    print(contador)

print("\n Bucle while con else")
contador = 0

while contador < 5:
    print(contador)
    contador += 1
else:
    print("El bucle ha terminado")

numero = -1

while numero < 0:
    numero = int(input("Escribe un nuúmero positivo: "))
    if numero < 0:
        print("El número debe ser positivo. Intenta otra vez, majo o maja.")

print(f"El número que has introducido es {numero}")

numero = -1

while numero < 0:
    try:
        numero = int(input("Escribe un número positivo: "))
        if numero < 0:
            print("El número debe ser positivo. Intenta otra vez")
    except:
        print("Lo que introduces debe ser un número")

print(f"El número que has introducido es: {numero}")

# EJERICIOS WHILE - JORGE ROBERTO NOVELO POOT

# Ejercicio 1: Cuenta atrás

contador = 10
while contador >= 1:
    print(contador)
    contador -= 1


# Ejercicio 2: Suma de números pares

suma = 0
numero = 1
while numero <= 20:
    if numero % 2 == 0:
        suma += numero
    numero += 1
print("La suma de los números pares es: ", suma)


# Ejercicio 3: Factorial de un número

n = int(input("Introduce un número entero positivo: "))
factorial = 1
temp = n

while temp > 0:
    factorial *= temp
    temp -= 1

print(f"El factorial de {n} es: {factorial}")

# Ejercicio 4: Validación de contraseña

contrasenia = ""
while len(contrasenia) < 8:
    contrasenia = input("Intrduce una contraseña (mínimo 8 caracteres): ")
    if len(contrasenia) < 8:
        print("Error, la contraseña es demasiado corta")

print("contraseña valida")

# Ejercicio 5: Tabla de multiplicar

num_tabla = int(input("Introduce un número para ver su tabla: "))
i = 1
while i <= 10:
    resultado = num_tabla * i
    print(f"{num_tabla} x {i} = {resultado}")
    i += 1

# Ejercicio 6: Números primos hasta N

n_limite = int(input("Introduce un número entero positivo N: "))
numero_actual = 2

print(f"Números primos hasta {n_limite}:")
while numero_actual <= n_limite:
    es_primo = True
    divisor = 2
    
    while divisor * divisor <= numero_actual:
        if numero_actual % divisor == 0:
            es_primo = False
            break
        divisor += 1
    
    if es_primo:
        print(numero_actual, end=" ")
        
    numero_actual += 1