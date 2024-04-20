# Ejercicio 10: Definir una función llamada calculo_transporte que reciba cuatro números: la
# cantidad de alumnos de 1era, 2da y 3er. salita de un jardín de infantes y la cantidad de
# asientos del transporte escolar. La función debe retornar cuántos micros necesito contratar
# para una excursión sabiendo que cada salita es acompañada por tres adultos.

import math

def calculo_transporte(cant_1ra, cant_2da, cant_3ra, nro_asientos):
    total_personas = cant_1ra + cant_2da + cant_3ra + 3 * 3 
    total_bondis = total_personas / nro_asientos
    total_bondis_redondeado = math.ceil(total_bondis + 0.5)
    return total_bondis_redondeado

cantidad_de_infantes = [22, 18, 20]
asientos_disponibles = 30

print(f"Cantidad de infantes: {sum(cantidad_de_infantes)}")
print(f"Cantidad de Acompañantes: {3 * 3}")
print(f"Cantidad de colectivos: {calculo_transporte(cantidad_de_infantes[0], cantidad_de_infantes[1], cantidad_de_infantes[2], asientos_disponibles)}")