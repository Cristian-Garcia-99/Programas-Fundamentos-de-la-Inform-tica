#Ejercicio 15: Pedir un verbo en infinitivo y mostrar su terminación (ar, er o ir)

palabra = input("Ingrese verbo en invinitivo: ")

print(len(palabra)) #jugar 5 letras, len() devuelve 5
print(palabra[len(palabra) - 2] + palabra[len(palabra) - 1])