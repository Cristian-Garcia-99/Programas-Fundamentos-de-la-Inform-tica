# Ejercicio 16: Pedir nombre, apellido, nro. de alumno y comisión que desea suscribirse.
# Mostrar el siguiente mensaje “La solicitud de inscripción a la comisión <comision>
# solicitada por el alumno <apellido>, <nombre> está siendo procesada”

nombre = input("Ingrese Nombre: ")
apellido = input("Ingrese Apellido: ")
comision = input("Ingrese comision: ")

print("La solicitud de la inscripcion a la comisión " + comision + " solicitada por el alumno " + apellido + ", " + nombre + " está siendo procesada")