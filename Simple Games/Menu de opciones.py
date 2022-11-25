import os
print ("Bienvenido!")
print ("Que archivo desea visitar? ")
eleccion = int (input ("1 - Generador de contraseñas \n2 - Advinador de numeros \n3 - Piedra Papel o tijera\n"))
os.system ("clear")
if (eleccion == 1):
    print ("La contreseña generada es: ")
    import passwordGenerator
elif (eleccion == 2):
    import numberGuesser
elif (eleccion == 3):
    import rockPaperScissors
