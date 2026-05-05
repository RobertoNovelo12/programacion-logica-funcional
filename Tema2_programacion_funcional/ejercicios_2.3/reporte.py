# ─────────────────────────────────────────────────────────────────────────────
#  Sección 1 — INVESTIGA
# ─────────────────────────────────────────────────────────────────────────────

# 1. ¿Qué es una función de primera clase en Python?
# R: Es una función que se puede tratar como cualquier otra variable:
#    se puede asignar a una variable, pasar como argumento y devolver desde otra función.

# 2. ¿Cuál es la diferencia entre una función de orden superior y un callback?
# R: Una función de orden superior es la que recibe o devuelve funciones.
#    Un callback es la función que se pasa como argumento y se ejecuta dentro de otra.

# 3. ¿Cuándo conviene usar comprensión de listas en lugar de un ciclo for?
# R: Cuando queremos crear listas de forma más corta, clara y eficiente.

# 4. ¿Qué hace map() y cómo se relaciona con lambda?
# R: map() aplica una función a cada elemento de un iterable.
#    lambda permite crear funciones rápidas sin nombre para usar con map().

# 5. ¿Qué ventaja ofrece pasar una función como argumento a otra función?
# R: Permite reutilizar código y hacer funciones más flexibles y dinámicas.

# ─────────────────────────────────────────────────────────────────────────────
# Sección 2 — PLANEA
# ─────────────────────────────────────────────────────────────────────────────

# Funciones necesarias:
# - preparar_pizza()
# - preparar_agua()
# - preparar_tamal()
# - calcular_promocion(cantidad)
# - tomar_orden(preparar_alimento, cantidad, precio_unitario)

# Función de orden superior:
# - tomar_orden → porque recibe otra función como argumento

# Comprensión de listas:
# - Para generar las porciones

# lambda + map():
# - Para calcular la lista de precios

# ─────────────────────────────────────────────────────────────────────────────
# Sección 3 — CODIFICA
# ─────────────────────────────────────────────────────────────────────────────

# ── PASO 1 ─────────────────────────────────────────────────────────────

def preparar_pizza():
    return "🍕 pizza"

def preparar_agua():
    return "🥤 agua fresca"

def preparar_tamal():
    return "🫔 tamal"


# ── PASO 2 ─────────────────────────────────────────────────────────────

def calcular_promocion(cantidad):
    if cantidad >= 3:
        return "🎁 postre gratis"
    return ""


# ── PASO 3 ─────────────────────────────────────────────────────────────

def tomar_orden(preparar_alimento, cantidad, precio_unitario):
    # a) Comprensión de listas
    porciones = [preparar_alimento() for _ in range(cantidad)]

    # b) map() + lambda
    precios = list(map(lambda x: precio_unitario, porciones))

    # c) Promoción
    promocion = calcular_promocion(cantidad)

    return porciones, precios, promocion


# ── PASO 4 ─────────────────────────────────────────────────────────────

cantidad_pizzas  = int(input("¿Cuántas pizzas deseas ordenar? "))
cantidad_aguas   = int(input("¿Cuántas aguas frescas deseas ordenar? "))
cantidad_tamales = int(input("¿Cuántos tamales deseas ordenar? "))

orden_pizza  = tomar_orden(preparar_pizza,  cantidad_pizzas,  25)
orden_agua   = tomar_orden(preparar_agua,   cantidad_aguas,   10)
orden_tamal  = tomar_orden(preparar_tamal,  cantidad_tamales, 15)


# ── PASO 5 ─────────────────────────────────────────────────────────────

print("\n========== RESUMEN DEL PEDIDO ==========")

porciones_pizza,  precios_pizza,  promo_pizza  = orden_pizza
porciones_agua,   precios_agua,   promo_agua   = orden_agua
porciones_tamal,  precios_tamal,  promo_tamal  = orden_tamal

print(f"\n🍕 PIZZAS   → {porciones_pizza}")
print(f"💲 Precios  → {precios_pizza}")
print(f"🎁 Promo    → {promo_pizza if promo_pizza else 'sin promoción'}")

print(f"\n🥤 AGUAS    → {porciones_agua}")
print(f"💲 Precios  → {precios_agua}")
print(f"🎁 Promo    → {promo_agua if promo_agua else 'sin promoción'}")

print(f"\n🫔 TAMALES  → {porciones_tamal}")
print(f"💲 Precios  → {precios_tamal}")
print(f"🎁 Promo    → {promo_tamal if promo_tamal else 'sin promoción'}")

print("\n========================================")

# ─────────────────────────────────────────────────────────────────────────────
# Desafío extra (opcional)
# ─────────────────────────────────────────────────────────────────────────────
# Si terminaste antes y quieres ir más allá:
#
# 1. Usa sum() y map() + lambda para calcular el TOTAL a pagar de cada orden.
# 2. Crea una función elegir_producto(nombre) que sea de ORDEN SUPERIOR:
#    recibe un string ("pizza", "agua" o "tamal") y DEVUELVE la función
#    de preparación correspondiente (sin ejecutarla).
#    Referencia: funciones.py → elegir_operacion()
# 3. Usa la función del punto 2 para reemplazar los argumentos directos en
#    las llamadas a tomar_orden().