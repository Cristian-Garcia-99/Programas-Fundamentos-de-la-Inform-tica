# Ejercicio 14: Definir tres funciones llamadas convertir_a_dolar, convertir_a_euro y
# convertir_a_real. Cada función recibe un parámetro que representa un monto en pesos y
# devuelve su conversión respectiva.

def convertir_a_dolar(monto):
    valor_dolar_peso = 800 
    return monto / valor_dolar_peso

def convertir_a_euro(monto):
    valor_euro_peso = 500
    return monto / valor_euro_peso

def convertir_a_real(monto):
    valor_real_peso = 50
    return monto / valor_real_peso

monto = 1000

print(f"{monto} pesos son {convertir_a_dolar(monto)} dolares")
print(f"{monto} pesos son {convertir_a_euro(monto)} euros")
print(f"{monto} pesos son {convertir_a_real(monto)} reales")