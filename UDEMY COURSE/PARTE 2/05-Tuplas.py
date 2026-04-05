"""
Las tuplas en Python son estructuras de datos ordenadas e inmutables (no se pueden modificar tras su creación), 
definidas mediante paréntesis () y elementos separados por comas. Son más rápidas y seguras que las listas, 
ideales para almacenar datos constantes, con acceso por índice y capacidad de desempaquetado.

Las tuplas pueden contener cualquier tipo de dato (enteros, cadenas, flotantes, etc), incluyendo otras tuplas, listas y diccionarios.
"""

# Tupla con números enteros
tupla_numeros = (1, 2, 3)

# Tupla con cadenas de texto
tupla_cadenas = ("manzana", "banana", "cereza")

# Tupla mixta con diferentes tipos de datos
tupla_mixta = (1, "Hola", 3.14)

# Tupla vacía
tupla_vacia = ()

print(tupla_numeros)
# También se puede mostrar un elemento específico de la tupla utilizando su índice (comenzando desde 0)
print(tupla_numeros[0])
print(tupla_cadenas[1])
print(tupla_mixta[2])
print(tupla_vacia)

print("\n\nAhora creamos una tupla de tuplas, donde cada tupla interna representa a una persona con su nombre y edad: ")

personas = (("Juan", 25), ("Maria", 16), ("Carlos", 20))
for nombre, edad in personas:
    if edad < 18:
        print(nombre, edad)
        
# Creamos una tupla de números enteros
numeros = (10, 20, 30, 40, 50, 100, 5000, 100000)

# La función sum() se utiliza para calcular la suma de todos los elementos en la tupla "numeros"
suma = sum(numeros)
print("La suma de los numeros es:", suma)