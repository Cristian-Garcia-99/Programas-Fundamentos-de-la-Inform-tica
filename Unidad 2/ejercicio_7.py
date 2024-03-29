# Ejercicio 7: Pedir el diámetro de un círculo y calcular su área y perímetro. Recordar
# que Perímetro = π * Diámetro , Área = π * radio2
# . Por último, el diámetro = 2 * radio

import math

pi = math.pi

diametro = int(input("Ingrese el diametro del círculo: "))
radio = diametro / 2

perimetro = pi * diametro
area = radio ** 2 * pi 

print("El valor del perimetro es: ", perimetro)
print("El valor del área es: ", area)