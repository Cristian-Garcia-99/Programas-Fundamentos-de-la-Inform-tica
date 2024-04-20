# Ejercicio 7: Definir una función que calcule el área de un círculo, otra que calcule el área de
# un rectángulo y otra que calcule el área de un cuadrado. Analice qué parámetros deberían
# recibir dichas funciones.

import math

def area_rectángulo(base, altura):
    return base * altura

def area_cuadrado(lado):
    return lado ** 2

def area_circulo(radio):
    return math.pi * radio ** 2

print(f"El área de un cuadrado de rectángulo de 2cm de base por 2cm de altura es: {area_rectángulo(2, 2)} cm^2")
print(f"El área de un cuadrado de 2cm de lado es: {area_cuadrado(2)} cm^2")
print(f"El área de un  círculo de 2cm de radio es: {area_circulo(2)} cm^2")