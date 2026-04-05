nombre = "Marco"
apellido = "Mendoza"
frase = "Hola esta es una frase"

longitud = len(frase)
print(longitud)

print(apellido[6])

palabras = frase.split()
print(palabras)

mayusculas = frase.upper()
print(mayusculas)

minuscula = apellido.lower()
print(minuscula)

mensaje = "Hola Mundo"
print(mensaje)

cambio_mensaje = mensaje.replace("Hola", "Marco")
print(cambio_mensaje)

for x in apellido:
    print(x)