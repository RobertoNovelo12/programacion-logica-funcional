from os import system
if system("clear") != 0: system("cls")

nombre = input("Hola, ¿cómo te llamas?\n")
print(f"Haola {nombre}, encantado de conocerte")

age = input("¿Cuántos años tienes?\n")
age = int(age)
print(f"Tienes {age} años")

print("Obtener multiples valores a la vez")
country, city = input("¿En qué país y ciudad vives?\n").split()

print(f"Vives en {country}, {city}")