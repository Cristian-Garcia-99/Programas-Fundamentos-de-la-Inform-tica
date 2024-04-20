# Ejercicio 12: Definir una función llamada calculo_litros que reciba tres números, el alto,
# ancho y profundidad (en metros) de una pileta y devuelva la cantidad de litros que tiene.

def calculo_litros(alto, ancho, profundidad):
    volumen_metros_cubicos = alto * ancho * profundidad
    volumen_litros = volumen_metros_cubicos * 1000 # Ya que 1 m^3 = 1000 L
    return volumen_litros

alto = 2
ancho = 4
profundidad = 1.5

print(f"La pileta tiene {calculo_litros(alto, ancho, profundidad)} Litros")