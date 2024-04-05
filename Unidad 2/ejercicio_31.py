#Ejercicio 31: Pedir el cuit que tiene la siguiente forma xx/dni/x. Extraer y mostrar el dni.

cuit = input("Ingrese cuit con la forma XX/DNI/X: ")
filtro = cuit.split("/")
print(f"El DNI es {filtro[1]}")