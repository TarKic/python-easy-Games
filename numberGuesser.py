import random
contTries = 1
max = int (input ("Ingrese el numero maximo del juego: "))
numberToGuess = random.randint (1,max)
num = int (input ("Que numero es? "))
while (num != numberToGuess):
    contTries += 1
    print ("No, no es... Esta es tu chance", contTries)
    num = int (input ("Que numero es? "))
print ("Felicitaciones! Adivinaste!")