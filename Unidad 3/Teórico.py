'''
PARTE I : Aspectos Conceptuales
a) ¿Qué ventajas tiene la utilización de funciones?
b) ¿Hay algún cuidado en el orden en el que se pasan los parámetros a una función?
c) ¿Cuándo uso la sentencia return?
d) ¿Qué diferencia hay entre la definición y la invocación de una función?
e) ¿Qué son los parámetros formales y para qué sirven? Ejemplifique.
f) ¿Qué son los parámetros reales y para qué sirven? Ejemplifique.
g) ¿Qué es el cuerpo de una función? Ejemplifique.
h) ¿Existen funciones sin parámetros o argumentos?
i) ¿Puede usar una letra o un número como parámetro formal? ¿Y como parámetro
real?
j) ¿Puedo tener una cantidad distinta de parámetros formales que reales en una
función?
k) ¿Cómo se puede implementar un módulo con solo definiciones de funciones e
importarlo desde tu programa? ¿Cuáles son las formas de importar que ofrece
Python?
l) ¿Qué diferencias hay entre los siguientes códigos?
i) import math
ii) from math import sqrt

'''

'''
a) Utilizar funciones tiene la utilizad de reutilizar código, ya que se programa una vez y se puede llamar múltiples veces.

b) Al pasar los parámetros invocando una función hay que respetar el orden en la que esta ha sido definida. 

c) La sentencia return se utiliza sólo si la función requiere una devolución.

d) Definir la función es programarla de manera genérica por primera vez. Invocarla es ejecutarla y darle un uso específico.

e) Los parámetros formales son variables locales dentro de la función.

f) Los parámetros reales son los que se pasan en el argumento de la invocación de una función.

g) El cuerpo de una función es todo lo que sigue después del encabezado y los dos puntos del mismo, es la parte funcional de la función.

h) Si existen funciones sin argumentos, por ejemplo se puede crear una funcion que al llamarla sólo imprima un mensaje que no dependa de variables.

i) Como parámetros fomales solo puedo usar variables, puesto que son las que va a recibir la función. Como parámetros reales se pueden enviar numeros directos, o numeros cargados en una variable.

j) No es correcto tener una disparidad entre los parámetros reales y formales, si la función está mal definida y utiliza menos parámetros de los que pide es posible, pero es un error de diseño.

k) Se pueden importar módulos para usar sus funciones con la sintaxis <import múdulo>, y luego usar sus funciones con la sintáxis <módulo.funcion(parámetros)>

l) <import math> importa el módulo completo. <from math import sqrt> importa únicamente la funcion sqrt del módulo math.

'''