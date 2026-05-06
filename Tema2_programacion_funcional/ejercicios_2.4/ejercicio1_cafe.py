def preparar_cafe():
    return "cafe"

def tomar_orden(numero_tazas):
    tazas_cafe = [preparar_cafe() for _ in range(numero_tazas)]
    return tazas_cafe


cafe_para_grupo = tomar_orden(10)
print(cafe_para_grupo)