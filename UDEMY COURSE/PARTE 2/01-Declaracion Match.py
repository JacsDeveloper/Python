numero = int(input("Ingrese un numero entero:"))

match numero:
    case 0: 
        print("El numero es un cero")
    case numero if numero % 2 == 0:
        print("El numero es par.")
    case numero if numero % 2 != 0:
        print("Es un numero impar.")
    case _:
        print("Numero no reconocido")