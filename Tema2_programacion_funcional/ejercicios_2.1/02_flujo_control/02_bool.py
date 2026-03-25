# Jorge Roberto Novelo Poot - 8B
###
# 02 - Booleanos
# Valores lógicos: True (verdadero) y False (falso).
# Fundamentales para el control de flujo y la lógica en programación.
###

from os import system
if system("clear") != 0: system("cls")

# Los booleanos representan valores de verdad: True o False.
print("\nValores booleanos basicos:")
print(True)
print(False)

# Operadores de comparacion: devuelven un valor booleano.
print("\nOperadores de comparación:")
print("5 > 3:", 5 > 3)
print("5 < 3:", 5 < 3)
print("5 == 5:", 5 == 5)
print("5 != 3:", 5 != 3)
print("5 >= 5:", 5 >= 5)
print("5 <= 3:", 5 <= 3)

print("\nComparación de cadenas:")
print("'manzana' < 'pera':", "manzana" < "pera") # True
print("'Hola' == 'hola'", "Hola" == "hola") # False

# Operadores logicos: and, or, not
print("\nOperadores logicos:")
print("True and True:", True and True)
print("True and False:", True and False)
print("True or False:", True or False)
print("False or False:", False or False)
print("not True:", not True)
print("not False:", not False)

# Tablas de verdad (para referencia):
print("\nTablas de verdad:")

print("\n and:")
print("A      B      A and B")
print("True   True ", True and True)
print("True   False", True and False)
print("False  True ", False and True)
print("False  False", False and False)

print("\n or:")
print("A      B      A or B")
print("True   True ", True or True)
print("True   False", True or False)
print("False  True ", False or True)
print("False  False", False or False)

print("\n not:")
print("A      not A")
print("True ", not True)
print("False", not False)