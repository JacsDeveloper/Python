"""
Un módulo es un archivo que contiene código Python. Un módulo puede definir funciones, clases y variables. 
También puede incluir código ejecutable. El código en el módulo se ejecuta una vez cuando se importa el módulo por primera vez.
Es una forma de organizar el código en archivos separados para mejorar la legibilidad y la reutilización.
Se puede interpretar como cuando uno importa una librería o biblioteca, lo que hace es importar un módulo. 
Por ejemplo, cuando importamos la biblioteca math, estamos importando el módulo math que contiene funciones matemáticas como sqrt, sin, cos, etc.

En este caso importamos un módulo llamado miprimermodulo.py que contiene funciones de operaciones matemáticas básicas como suma, resta y multiplicación. 
Este archivo llamado miprimermodulo.py debe estar en el mismo directorio que el archivo que contiene el código de este ejercicio para que pueda ser importado correctamente.
"""

import miprimermodulo

numero1 = int(input("Introduce un número:"))
numero2 = int(input("Ahora introduce un segundo número:"))

# Con . se accede a las funciones definidas en el módulo importado. (Por ejemplo, miprimermodulo.suma(variable1, variable2)
suma = miprimermodulo.suma(numero1, numero2)
resta = miprimermodulo.resta(numero1, numero2)
multiplicacion = miprimermodulo.multiplicacion(numero1, numero2)
print(suma)
print(resta)
print(multiplicacion)