# Ejercicio 16: Definir una función llamada precio_con_iva que agrega el IVA (21%) de un
# producto dado su precio de venta sin IVA.

def precio_con_iva(monto):
    return monto * 1.21

print(f"Monto: 100 $ / Monto con IVA: {precio_con_iva(100)} $")
print(f"Monto: 500 $ / Monto con IVA: {precio_con_iva(500)} $")