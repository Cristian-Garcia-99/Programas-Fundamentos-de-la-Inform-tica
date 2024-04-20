# Ejercicio 13: Definir una función llamada a_pagar que reciba 4 números: la cantidad de
# personas, el monto gastado en bebida, el monto gastado en comida y el del alquiler del
# lugar, y retorne cuánto le toca pagar a cada uno.

def a_pagar(cantidad_personas, monto_bebidas, monto_comida, monto_alquiler):
    return (monto_alquiler + monto_bebidas + monto_comida) / cantidad_personas

gasto_bebidas = 100
gasto_comida = 300
gasto_alquiler = 100
amigos = 4

print(f"El total a oagar entre los {amigos} amigos es de {a_pagar(amigos, gasto_bebidas, gasto_comida, gasto_alquiler)} $")