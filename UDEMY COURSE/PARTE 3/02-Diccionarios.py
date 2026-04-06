"""
Los diccionarios son una estructura de datos en Python que permiten almacenar pares de clave-valor. 
Son mutables, lo que significa que se pueden modificar después de su creación. 
Los diccionarios se definen utilizando llaves {} y cada par de clave-valor se separa por dos puntos (:). 
Las claves deben ser únicas dentro del diccionario, mientras que los valores pueden ser de cualquier tipo de dato.
"""

personas = {
    "persona1":{
        "nombre": "Juan",
        "edad": 30,
        "ciudad": "Madrid"
    },
    "persona2":{
        "nombre": "Maria",
        "edad": 28,
        "ciudad": "Barcelona"
    },
    "persona3":{
        "nombre": "Carlos",
        "edad": 35,
        "ciudad": "Valencia"
    }
}

# Acceder a los datos de cada persona. Se debe declarar una variable para cada persona, y luego acceder a cada dato utilizando la clave correspondiente.
datos = personas["persona1"]
datos2 = personas["persona2"]
datos3 = personas["persona3"]
 
print(datos["nombre"])
print(datos2["edad"])
print(datos3["ciudad"])


# Crear un diccionario para almacenar los datos de una persona, solicitandoal usuario que ingrese los datos de la persona con la función input().
persona1  = {
    "nombre": None,
    "edad": None,
    "direccion": None,
    "telefono": None,
}

persona1["nombre"]= input("Introduce un nombre:")
persona1["edad"]= input("Introduce tu edad:")
persona1["direccion"]= input("Introduce tu direccion:")
persona1["telefono"]= input("Introduce tu telefono:")

print(persona1["nombre"], "tiene", persona1["edad"], "años, vive en", persona1["direccion"], "y su numero de telefono es", persona1["telefono"])