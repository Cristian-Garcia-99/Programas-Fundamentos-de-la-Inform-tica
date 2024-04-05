# Ejercicio 20:Ejecutar los siguientes códigos. ¿Cuál es el resultado de las siguientes
# ejecuciones?. Justificar

#-------------------------------------------------

# tupla = (1,True,['a','b','c'], "hola")
# tupla[1] = False

#El resultado es un TypeError ya que la tupla no es modificable  por lo que no admite una asignación de item para modificar un valor

#-------------------------------------------------

# tupla = (1,True,['a','b','c'], "hola")
# tupla[2][0] = 'b'
# print(tupla)

#El resultado es la tupla con su lista modificada, si bien la tupla en si no es modificable, puede modificar los elementos de una lista que tenga contenida