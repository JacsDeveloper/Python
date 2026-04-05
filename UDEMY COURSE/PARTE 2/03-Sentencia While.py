contador = 1
while contador <= 10:
    print(contador)
    contador += 1
print("Fin del ciclo ... Vamos con otro ejemplo !! \n\n")

print("Contador descendente")
contador = 10
while contador >= 1:
    print(contador)
    contador -= 1
print("Feliz año nuevo !! ... Vamos con otro ejemplo !! \n\n")

print("Suma de números positivos ingresados por el usuario")

suma = 0
numero = int(input("Ingrese un número positivo (o un número negativo para terminar): "))
while numero >= 0:
    suma += numero
    numero = int(input("Ingrese un número positivo (o un número negativo para terminar): "))
print("La suma de los números positivos ingresados es:", suma)