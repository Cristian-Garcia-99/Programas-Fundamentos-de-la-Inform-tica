# Ejercicio 26: Ejecute el siguiente código e indique, en cada caso, con qué valor finaliza
# la variable x. Justifique su respuesta.

#-------------------------------------

# x = 10
# X = x**2
# print(x)

#La variable termina con el valor 10 puesto que se imprime x minúscula y python diferencia las minúsculas de las mayúsculas.

#-------------------------------------

# x = 30
# # x = x % 4
# print(x)

#Se imprime 30 ya que la segunda línea está comentada, por lo que no se ejecuta.

#-------------------------------------

# a = "4"
# b = "3"
# x = a + b
# print (x)

#Se imprime 43 puesto que a y b son cadenas, por lo que el operador + actúa como concatenador

#-------------------------------------


# a = "4"
# b = 3
# x = a * b
# print (x)

#Se imprime 444 puesto que el valor de a es un str y el valor de b es un int, por lo que el operador * actúa como un multiplicador de cadena

#-------------------------------------

a = 4
b = 3
x = "a" * b
print(x)

#Se imprime aaa puesto que el valor de b es un int, y al poner "a" se ejecuta como un multiplicador de cadena, puesto que NO se hace referencia al valor de la variable a, sino a un str nuevo