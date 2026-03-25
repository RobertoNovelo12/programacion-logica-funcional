from os import system
if system("clear") != 0: system("cls")

print("Conversión de tipos")

print(int("100")+2) #convierte "100" a entero y suma 2
print("100"+str(2))

print((type(float("3.1416"))))

print(int(3.1416))

print(bool(3))
print(bool(0))
print(bool(-1))

print(bool(""))
print(bool(" "))
print(bool("False"))


print(round(2.51))

print(int("Hola mundo"))