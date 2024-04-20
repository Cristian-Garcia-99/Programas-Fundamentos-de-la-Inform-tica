# Ejercicio 8: Definir una función llamada calculo_rebaja que reciba dos números, uno con
# el precio anterior y otro para el precio rebajado y devuelva un número que represente el
# porcentaje rebajado.

def calculo_rebaja(precio_anterior, precio_rebajado):
    diferencia = precio_rebajado - precio_anterior
    porcentaje = (diferencia / precio_anterior) * 100
    return porcentaje

print("Precio anterior: 10")
print("Precio rebajado: 8")
print(f"Porcentaje reducido: {calculo_rebaja(10, 8)}%")