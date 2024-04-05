# Ejercicio 33: Pedir la cuenta de mail al usuario y mostrar por separado su usuario y su dominio.

mail = input("Ingrese mail: ")
usuario, dominio = mail.split("@")

print(f"El usuario es {usuario} y su dominio es {dominio}")

#GUARDANDOLO ÚNICAMENTE EN UNA LISTA EL PROGRAMA QUEDA: 
# filtro = mail.split("@")
# print(f"El usuario es {filtro[0]} y su dominio es {filtro[1]}")