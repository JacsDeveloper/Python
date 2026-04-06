class Calculadora1:
    def __init__(self, numero):
        self.resultado = numero

    def sumar(self, numero):
        self.resultado += numero

    def restar(self, numero):
        self.resultado -= numero
    
    def multiplicar(self, numero):
        self.resultado *= numero

    def dividir(self, numero):
        if numero != 0:
            self.resultado /= numero
        else:
            print("Error: Nose puede dividir por cero.")
    
    def resultado(self):
        return self.resultado
    
calculo = Calculadora1(0)

calculo.sumar(5)
calculo.multiplicar(4)
calculo.restar(5)
calculo.dividir(2)

resultado = calculo.resultado
print("Resultado:", resultado)


class Calculadora2:
    def suma(self, num1, num2):
        return num1 + num2
    
    def resta(self, num1, num2):
        return num1 - num2
    
    def multiplicar(self, num1, num2):
        return num1 * num2
    
    def divicion(self, num1, num2):
        if num2 == 0:
            return "Error: No se puede dividir por cero."
        
num1 = float(input("Ingresa el primer numero:"))
num2 = float(input("Ingresa el segundo numero:"))

calc = Calculadora2()

resulsuma = calc.suma(num1, num2)
resulresta = calc.resta(num1, num2)
resulmultiplicacion = calc.multiplicar(num1, num2)
resuldivision = calc.divicion(num1, num2)

print("Suma:", resulsuma)
print("Resta:", resulresta)
print("Multiplicación:", resulmultiplicacion)
print("División:", resuldivision)