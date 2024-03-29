# Ejercicio 11: Pedir datos de 4 productos comprados, con su cantidad y precio unitario
# y mostrar cuánto se gasta por cada producto y el total

print("PRODUCTO 1")
cantidad_1 = int(input("Ingrese cantidad: "))
precio_1 = int(input("Ingrese precio: "))
costo_1 = cantidad_1 * precio_1

print("\nPRODUCTO 2")
cantidad_2 = int(input("Ingrese cantidad: "))
precio_2 = int(input("Ingrese precio: "))
costo_2 = cantidad_2 * precio_2

print("\nPRODUCTO 3")
cantidad_3 = int(input("Ingrese cantidad: "))
precio_3 = int(input("Ingrese precio: "))
costo_3 = cantidad_3 * precio_3

costo_total = costo_1 + costo_2 + costo_3

print("\nDel producto 1 gastó: ", costo_1)
print("Del producto 2 gastó: ", costo_2)
print("Del producto 3 gastó: ", costo_3)
print("El gasto total es: ", costo_total)

