# Ejercicio 6: Definir una función que reciba un número como parámetro y mostrar la tabla de
# multiplicar de dicho número.

def tabla_de_multiplicar(numero):
    print("-" * 6)
    print(f"Tabla del {numero}")
    print(f"""
    {numero} X 1 = {numero * 1}
    {numero} X 2 = {numero * 2}
    {numero} X 3 = {numero * 3}
    {numero} X 4 = {numero * 4}
    {numero} X 5 = {numero * 5}
    {numero} X 6 = {numero * 6}
    {numero} X 7 = {numero * 7}
    {numero} X 8 = {numero * 8}
    {numero} X 9 = {numero * 9}
    {numero} X 10 = {numero * 10}""")

tabla_de_multiplicar(3)
print()
tabla_de_multiplicar(333)