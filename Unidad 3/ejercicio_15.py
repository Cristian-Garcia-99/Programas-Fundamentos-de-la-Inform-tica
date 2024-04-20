# Ejercicio 15: Definir una función llamada calculo_dosis que reciba tres números. Uno para
# la cantidad de días que debe suministrarse el remedio, el segundo dato para la cantidad de
# veces por día que debe tomarlo, y el último dato para la cantidad de comprimidos que trae el
# envase. La función debe devolver verdadero si el envase alcanza para ese tratamiento y
# falso si no alcanza.

def calculo_dosis(total_dias, comprimidos_por_dia, cantidad_comprimidos):
    comprimidos_totales_requeridos = comprimidos_por_dia * total_dias
    
    if cantidad_comprimidos >= comprimidos_totales_requeridos:
        return True
    else:
        return False
    
dias_tratamiento = 10
capsulas_por_dia = 2
capsulas_totales = 19

print("El tratamiento se puede completar" if calculo_dosis(dias_tratamiento, capsulas_por_dia, capsulas_totales) 
      else "El tratamiento no se puede completar") 