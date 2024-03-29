# Ejercicio 9: Pedir alto, ancho y largo de una pileta. Calcular el volumen y la cantidad
# de litros que tiene. (saber que 1000 cm3=1 litro)

alto = int(input("Ingrese la altura de la pileta en metros: "))
largo = int(input("Ingrese la longitud de la pileta en metros: "))
ancho = int(input("Ingrese el ancho de la pileta en metros: "))

volumen = alto * largo * ancho
litros = volumen * 1000 #Ya que 1m^3 * (1000dm^3 / 1m^3) y 1L = 1dm^3 

print("En la pileta caben: ", litros, " litros")
