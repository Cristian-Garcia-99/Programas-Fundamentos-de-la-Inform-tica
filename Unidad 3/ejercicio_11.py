# Ejercicio 11: Definir una función llamada armo_cartel que reciba una cadena de caracteres
# (para el nombre del producto) y dos números (el precio anterior y el otro para el precio
# rebajado) e imprima un cartel de la siguiente forma:
# *************************************
# Atención!!! Gran rebaja para el producto nombre (recibido como parámetro)
# Antes: precio anterior (dato recibido como parámetro)
# Ahora: precio rebajado (dato recibido como parámetro)

def armo_cartel(nombre_producto, precio_anterior, precio_rebajado):
    print("*" * 40)
    print(f"Atencion!!! Gran rebaja del producto {nombre_producto}")
    print(f"Antes: {precio_anterior} $")
    print(f"Ahora: {precio_rebajado} $")
    print("*" * 40)
    
armo_cartel("Dulce de Leche", 1425, 870)