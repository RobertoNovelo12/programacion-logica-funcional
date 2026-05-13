def preparar_hotcake():
    return "🥞"

def tomar_orden(numero_piezas):
    piezas_hotcakes = [preparar_hotcake() for _ in range(numero_piezas)]
    return piezas_hotcakes

hotcakes_familia = tomar_orden(int(input("¿Cuantos son en tu familia?:")))
print(hotcakes_familia)