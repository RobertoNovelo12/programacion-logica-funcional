###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumplen ciertas condiciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\n Sentencia simple condicional")
# Podemos usar la palabra clave "if" para ejecutar un bloque de codigo
# solo si se cumple una condición.
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
    print("¡Felicidades!")

# Si no se cumple la condición, no se ejecuta el bloque de código
edad = 15
if edad >= 18:
    print("Eres mayor de edad")
    print("¡Felicidades!")

# Podemos usar el comando "else" para ejecutar un bloque de código
# si no se cumple la condicion anterior del if
print("\n Sentencia condicional con else")
edad = 15
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

print("\n Sentencia condicional con elif")
# Ademas de usar "if" y "else", podemos usar "elif" para determinar
# múltiples condiciones, ten en cuenta que sólo se ejecutará el primer bloque
# de código que cumpla la condición (o la del else, si está presente)
nota = 5
if nota >= 9:
    print("iSobresaliente!")
elif nota >= 7:
    print("Notable!")
elif nota >= 5:
    print("¡Aprobado!")
else:
    print("¡No está calificado!")

print("\n Condiciones múltiples")
edad = 16
tiene_carnet = True

# Los operadores logicos en Python son:
# and: True si ambos operandos son verdaderos
# or: True si al menos uno de los operandos es verdadero
# En JavaScript:
# && sería and
# || sería or

# En el caso que seas mayor de edad y tengas carnet ...
# entonces podras conducir
if edad >= 18 and tiene_carnet:
    print("Puedes conducir")
else:
    print("POLICIA !!")

# En un pueblo de Isla Holbox son mas relajados y
# te dejan conducir si eres mayor de edad ó tienes carnet
if edad >= 18 or tiene_carnet:
    print("Puedes conducir en la Isla Holbox =")
else:
    print("Paga al policía y te dejara conducir !!! ")

# Tambien tenemos el operador logico "not"
# que nos permite negar una condición
es_fin_de_semana = False
# JavaScript -> !
if not es_fin_de_semana:
    print("¡ISC, anda que hay que ir al Tec!")
# Podemos anidar condicionales, uno dentro del otro
# para determinar múltiples condiciones aunque
# siempre intentaremos evitar esto para simplificar
print("\n Anidar condicionales")
edad = 20
tiene_dinero = True

if edad >= 18:
    if tiene_dinero:
        print("Puedes ir a la discoteca")
    else:
        print("Quédate en casa")
else:
    print("No puedes entrar a la disco")

# Más fácil sería:
# if edad < 18:
# print("No puedes entrar a la disco")
# elif tiene_dinero:
# print("Puedes ir a la discoteca")
# else:
# print("Quédate en casa")

# Ten en cuenta que hay valores que al usarlos como condiciones
# en Python son evaluados como verdaderos o falsos
# por ejemplo, el número 5, es True
numero = 5
if numero: # True
    print("El número no es cero")

# Pero el número 0 se evalúa como False
numero = 0
if numero: # False
    print("Aquí no entrará nunca")

# También el valor vacío "" se evalúa como False
nombre = ""
if nombre:
    print("El nombre no es vacio")

# iTen cuidado con no confundir la asignación = con la comparación ==!
numero = 3 # asignación
es_el_tres = numero == 3 # comparación

if es_el_tres:
    print("El número es 3")

# A veces podemos crear condicionales en una sola linea usando
# las ternarias, es una forma concisa de un if-else en una línea de código
print("\nLa condición ternaria:")
# [código si cumple la condición] if [condicion] else [codigo si no cumple]

edad = 17
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)

###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos numeros
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

numero = int(input("Igresa un número: "))
numero2 = int(input("Igresa un segundo número: "))

if numero > numero2:
    print(f"El número mayor es: {numero}")
elif numero2 > numero:
    print(f"El número mayor es: {numero2}")
else:
    print(f"los números {numero} y {numero2} son iguales")

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

num1 = float(input("Escribe un número: "))
num2 = float(input("Escribe un segundo número: "))
opcion = int(input("Elige tu operación: 1. suma - 2. resta - 3. multiplicacion - 4. division: "))

if opcion == 1:
    print(f"El resultado es: {num1 + num2}")
elif opcion == 2:
    print(f"El resultado es: {num1 - num2}")
elif opcion == 3:
    print(f"El resultado es: {num1 * num2}")
elif opcion == 4:
    if num2 == 0:
        print("No se puede dividir entre 0")
    else:
        print(f"El resultado es: {num1 / num2}")
else:
    print("Opción inválida")

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

anio = int(input("Introduce un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print("Es un año bisiesto")
else:
    print("No es un año bisiesto")

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

edad = int(input("Introduce una edad: "))

if 0 <= edad <= 2:
    print("Bebé")
elif 3 <= edad <= 12:
    print("Niño")
elif 13 <= edad <= 17:
    print("Adolescente")
elif 18 <= edad <= 64:
    print("Adulto")
elif edad >= 65:
    print("Adulto mayor")
else:
    print("Edad no válida")