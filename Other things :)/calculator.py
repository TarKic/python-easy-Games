import math
def suma (numero1, numero2):
    resultado = numero1 + numero2
    return resultado

def resta (numero1,numero2):
    resultado = numero1 - numero2
    return resultado

def division (numero1, numero2):
    resultado = numero1 / numero2
    return resultado

def multiplicacion (numero1, numero2):
    resultado = numero1 * numero2
    return (resultado)

def potencia (numero1, numero2):
    resultado = numero1 ** numero2
    return resultado

def raiz (numero1, numero2):
    eleccion = int (input ("De que numero quiere hacer la raiz cuadrada: "))
    return (math.sqrt (eleccion))



print ("CALCULADORA")
num1 = int (input("Ingrese el primer numero: "))
num2 = int (input("Ingrese el segundo numero: "))
calculo = int (input ("\n1-Suma\n2-Resta\n3-Division\n4-Multiplicacion\n5-Potencia\n6-Raiz\n"))
if (calculo == 1):
    result = suma (num1,num2)
elif (calculo == 2):
    result = resta (num1,num2)
elif (calculo == 3):
    result = division (num1,num2)
elif (calculo == 4):
    result = multiplicacion (num1,num2)
elif (calculo == 5):
    result = potencia (num1,num2)
elif (calculo == 6):
    result = raiz (num1,num2)

print ("El resultado es:", result)