def preparar_cafe():
    return "cafe americano"

def preparar_olla():
    return "cafe de olla"
def ordenar_cafe(funcion_preparar, numero_tazas):
    tazas_cafe = [funcion_preparar() for _ in range(numero_tazas)]
    return tazas_cafe

cafe_grupo_a = ordenar_cafe(preparar_cafe, 12)
cafe_grupo_b = ordenar_cafe(preparar_olla, 10)

print(cafe_grupo_a, cafe_grupo_b)