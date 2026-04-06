"""
Ejemplo de clases y objetos en Python. En este ejemplo, se define una clase llamada "Persona" 
con un constructor __init__ (En Python se llama inicializador) que inicializa los atributos "nombre" y "edad". 
La clase también tiene un método llamado "saludar" que imprime un mensaje de saludo utilizando los atributos de la instancia.

Por convención, los nombres de las clases en Python se escriben con mayúscula inicial (CamelCase), 
mientras que los métodos y atributos se escriben con minúscula y guiones bajos (snake_case).
"""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Crear una instancia de la clase Persona
persona1 = Persona("Jacs", 33)

# Llamar al método saludar
persona1.saludar()

# Crear otra instancia de la clase Persona
persona2 = Persona("María", 25)

# Llamar al método saludar para la segunda persona
persona2.saludar()