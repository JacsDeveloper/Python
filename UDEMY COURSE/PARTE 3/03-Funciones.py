"""
Las funciones son bloques de código reutilizables que realizan una tarea específica. 
Se definen utilizando la palabra clave "def" seguida del nombre de la función y paréntesis que pueden contener parámetros. 
Las funciones pueden devolver un valor utilizando la palabra clave "return".
"""

# Función que suma dos números
def suma(a, b):
    resultado = a+b
    return resultado

numero1 = int(input("Introduce un numero:"))
numero2 = int(input("Introduce un segundo numero:"))

resultado = suma(numero1, numero2)
print(f"El resultado de la suma es: {resultado}.")

# Función que determina si un número es par o impar
def par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
numero = int(input("Introduce un número:"))
if par(numero) == True:
    print(f"{numero} es un número par.")
else:
    print(f"{numero} es un número impar.")

# Función que encuentra el valor máximo en una lista de números
def lista_numeros(lista):
    maximo = max(lista)
    return maximo

lista = [10, 40, 50, 55, 6]
valor_maximo = lista_numeros(lista)
print("El valor máximo almacenado en la  lista es:", valor_maximo)