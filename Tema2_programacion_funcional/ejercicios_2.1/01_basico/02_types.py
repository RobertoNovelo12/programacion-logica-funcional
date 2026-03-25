# Jorge Roberto Novelo Poot - 8B
from os import system

if system("clear") != 0: system("cls")

print("int:")

print(type(10))
print(type(0))
print(type(-5))
print(type(7091237489127389471273487123947120374))

print("float:")
print(type(3.14))
print(type(1.0))
print(type(1e3))


print("complex")
print(type(1 + 2j))

print("str:")
print(type("Hola"))
print(type(""))
print(type("123"))
print(type("""
Multilinea
"""))

print("bool")
print(type(True))
print(type(False))
print(type(1<2))

print("NoneTtype: ")
print(type(None))