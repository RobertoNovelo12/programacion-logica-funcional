# Jorge Roberto Novelo Poot - 8B
from os import system
if system("clear") != 0: system("cls")

print("\n range()")

# secuencia del 1 al 10

for num in range(5,10):
    print(num)

for num in range(0, 1000, 5):
    print(num)

for num in range(-5,0):
    print(num)

for num in range(10, 0, -1):
    print(num)

for num in range(0, 444):
    print(num)

nums = range(10)
list_of_nums = list(nums)
print(list_of_nums)

for _ in range(5):
    print("Hacer 5 veces algo")