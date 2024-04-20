# Ejercicio 9: Definir una función llamada calculo_nuevo_precio que reciba dos números,
# uno con el precio anterior y otro con el número de porcentaje a aumentar y devuelva el
# precio aumentado.

def calculo_nuevo_precioo(precio_anterior, porcentaje):
    nuevo_precio = precio_anterior * (1 + porcentaje / 100)
    return nuevo_precio


print("Precio actual: 100 $")
print("Porcentaje de aumento: 20%")
print(f"Precio aumentado: {calculo_nuevo_precioo(100, 20)} $")