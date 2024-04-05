# Ejercicio 29: Si se tiene las variables n1=124.25 y n2= “33.40”. Realizar las
# conversiones necesarias para saber la división entera entre ellos y el resto.

n1 = 124.25
n2 = "33.40"

t = float(n2)

div_entera = n1 // t
resto = n1 % t

print("División entera = ", div_entera)
print(f"Resto = {resto:.4f}")