# Ejercicio 5: Definir una función denominada cuantos_dias que reciba el número de mes
# como parámetro y retorne la cantidad de días que posee. Ejemplo: cuantos_dias(1),
# debería retornar 31. Ayuda: Pensar en tener una lista de la siguiente manera: [[“enero”,31],
# [“febrero”, 28], ...]

def cuantos_dias(mes):
    meses = [["Enero", 31], ["Febrero", 28], ["Marzo", 31], ["Abril", 30], ["Mayo", 31], ["Junio", 31]]
    mes_visto = meses[mes - 1]
    print(f"El mes {mes_visto[0]} tiene {mes_visto[1]} dias")
    
cuantos_dias(6)
cuantos_dias(1)
cuantos_dias(2)