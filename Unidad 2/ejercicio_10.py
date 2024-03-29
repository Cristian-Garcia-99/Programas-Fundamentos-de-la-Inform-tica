# Ejercicio 10: Pedir ancho y largo de un terreno y mostrar cuántos paneles de pasto
# hay que comprar (son de 60x60 cm)

largo = int(input("Ingrese la longitud del terreno en metros: "))
ancho = int(input("Ingrese el ancho del terreno en metros: "))

area_terreno = largo * ancho
area_placas = 0.6 * 0.6

cantidad_placas = int(area_terreno / area_placas)
print("Hay que comprar ", cantidad_placas, "placas de pasto")


