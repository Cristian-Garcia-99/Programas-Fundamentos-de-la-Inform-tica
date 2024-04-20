# Ejercicio 1: Dado el siguiente código indique cuáles son los parámetros reales y los formales:

'''
#Definicion de funciones

def sumaAlcuadrado(x, y):
    rta= x**2 + 2*x*y + y**2
    return rta

#Programa principal

print ("Bienvenidos/as a la Suma al Cuadrado")
a = input("Ingrese el valor de a: ")
b = input("Ingrese el valor de b: ")
print (sumaAlcuadrado(a, b))
'''

'''
Los parámetros formales son x e y que se encuentran como definición de la función
Los parámetros reales a y b que se cargan por el usuario

NOTA: El programa está MAL definido ya que no convierte los valores del input, por lo que a y b son del timpo STR. 
'''