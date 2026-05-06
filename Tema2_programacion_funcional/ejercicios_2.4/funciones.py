# ejemplo callback
def operar(n1, n2, funcion):
    return funcion(n1, n2)

def suma (a,b):
    return a + b

def resta (a,b):
    return a - b

resultado = operar(5, 3, suma)

print(resultado) # Imprime 8


'''
un callback es una función que se pasa como argumento a otra función y se ejecuta después de que se complete la tarea principal de esa función.
'''

# ejemplo funcion primer clase

def saludo():
    return "hola"                                       

mi_variable = saludo()
print(mi_variable) 


def saludo2():
    return "que tal"

mi_variable2 = saludo2
print(mi_variable2()) 


'''
una funcion de primer clase puede ser asignada a una variable, pasada como argumento a otra función, o incluso devuelta por otra función
'''

# ejemplo funcion de orden superior

def elegir_operacion(operacion):
    def multiplicacion(x):
        return x * 2
    def division(x):
        return x / 2
    
    if operacion == "multiplicar":
        return multiplicacion
    else:
        return division

doble = elegir_operacion("multiplicar")
print(doble(10))

divide2= elegir_operacion("dividir")
print(divide2(10))

#EJEMPLO DE FUNCIÓN = LAMBDA

doble = lambda x: x * 2
print(doble(5))

numeros = [1, 2, 3, 4]
dobles = list(map(lambda x: x * 2, numeros))
print(dobles)

alumnos = ['Alejandro', 'Miguel', 'Vinicio', 'Rodney', 'Marcial']
saludar_alumnos = list(map(lambda nombre: 'Hola' + nombre, alumnos))
print(saludar_alumnos)

def saludar(nombre):
    return 'Hola' + nombre

lista_saludos = list(map(saludar, alumnos))
print(lista_saludos)