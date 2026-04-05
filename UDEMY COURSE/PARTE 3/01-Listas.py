"""
Las listas se diferencian de las tuplas en que son mutables, es decir, se pueden modificar después de su creación. 
Las listas se definen utilizando corchetes [] y pueden contener elementos de diferentes tipos de datos.
"""

# Lista de números enteros
numeros = [1, 2, 3, 4, 5]

# Lista de cadenas de texto
frutas = ["manzana", "banana", "cereza"]

# Lista mixta con diferentes tipos de datos
mixta = [1, "hola", 3.14, True]

print(numeros[0])
print(frutas[1])

numeros[2] = 9
print(numeros[2])

numeros.append(8)
print(numeros)

frutas.append("coco")
print(frutas)

del numeros[2]
del frutas[0]
print(numeros)
print(frutas)


for fruta in frutas:
    print(fruta)

suma = sum(numeros)
print(suma)