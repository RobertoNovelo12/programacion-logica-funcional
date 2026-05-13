def preparar_pizza():
    return "🍕"

def preparar_hamburguesa():
    return "🍔"

def preparar_hotdog():
    return "🌭"

def dar_bonus(numero_porciones):
    return "Coca gratis" if numero_porciones > 2 else "";

def ordenar_alimento(preparar_alimento, numero_porciones):
    porciones_alimentos = [preparar_alimento() for _ in range(numero_porciones)]
    return porciones_alimentos, dar_bonus(numero_porciones)

grupo_1 = ordenar_alimento(preparar_pizza, 3)
grupo_2 = ordenar_alimento(preparar_hamburguesa, 2)
grupo_3 = ordenar_alimento(preparar_hotdog, 4)

print(grupo_1, grupo_2, grupo_3)