from random import randint

options = ["piedra" , "papel", "tijera"]
computer = options[randint (0,2)]
player = False

while player == False:
    player = input ("Piedra, papel o tijera: ")
    if (computer == player):
        print ("Empate!")
    elif (player == 'piedra'):
        if (computer == "tijera"):
            print ("Ganaste! la", player, "aplasta a la", computer)
        else:
            print ("Perdiste... El", computer, "enuvelve a la ", player)
    elif (player == "papel"):
        if (computer == 'tijera'):
             print ("Perdiste... La", computer, "corta al ", player)
        else:
            print ("Ganaste! El", player, "envuelve a la", computer)
    elif (player == "tijera"):
        if (computer == 'papel'):
            print ("Ganaste! La", player, "corta al", computer)
        else:
            print ("Perdiste... La", computer, "aplasta a la ", player)
    another = input ("Queres seguir jugando?: ")
    if (another == 'si' or 'Si'):
        player = False
        computer = options[randint (0,2)]

    player = True
