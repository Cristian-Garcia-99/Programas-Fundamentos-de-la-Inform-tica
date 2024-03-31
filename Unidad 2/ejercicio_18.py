# Ejercicio 18: Pedir nombre, apellido de una persona y el día, mes, año en que nació.
# Armarle una clave con esos datos (su clave seria sus iniciales seguido de un guión
# bajo y de su año de nacimiento) y mostrarla.

nombre = input("Ingrese nombre: ")
apellido = input("Ingrese apelido: ")
dia = input("Ingrese día de nacimiento: ")
mes = input("Ingrese mes de nacimiento: ")
año = input("Ingrese año de nacimiento: ")

clave = nombre[0] + apellido[0] + "_" + dia + "/" + mes + "/" + año

print(clave)