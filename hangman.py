import random

def buscaPalabras (): 
    try:
        arch = open ("palabras.txt", "rt")
    except IOError:
        print ("No se pudo abrir el archivo...")
    else:
        palabras = arch.readlines ()
        arch.close ()
        return palabras

def generaRenglones (a): 
    lista = []
    for i in range (len(a)-1):
        lista.append ("_ ") 
    return lista

def seleccionaPalabra (listaImportada): 
    palabraAdivinar = listaImportada[random.randint(0,len(lista) - 1)] 
    return palabraAdivinar

def dibujaPersona (intentos):  
    if intentos == 1:
         print("   _____ \n"
                  "  |     |\n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
    elif (intentos == 2):
        print("   _____ \n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
    elif (intentos == 3):
         print("   _____ \n"
                 "  |     | \n"
                 "  |     O \n"
                 "  |     |\ \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
    elif (intentos == 4):
        print("   _____ \n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
    elif (intentos == 5):
        print("   _____ \n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |      \ \n"
                  "__|__\n")
    elif (intentos == 6):
        print("   _____ \n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"    
                  "  |        \n"
                  "  |         \n"
                  "__|__\n")



cantidadDeJugadores = int (input ("Ingrese la cantidad de usuarios que jugaran: "))
yaJugaron = 0
listaParticipantes = []
listaPuntajes = []

while (yaJugaron < cantidadDeJugadores ):
    nombre = input ("Ingrese el nombre de la persona que jugara: ")
    listaParticipantes.append(nombre)
    yaJugaron += 1 #Sumador para indicar que un jugador comenzó un nuevo juego
    
    #Llamado a las funciones requeridas para el funcionamiento del programa
    lista = buscaPalabras ()
    palabra = seleccionaPalabra (lista)
    tablero = generaRenglones (palabra)
    chances = 6
    intentos = 0
    usoIntentos = 0
    cantidadLetras = len(palabra)-1 
    listasUtilizadas = [] 
    aciertos = 0

    while (chances > intentos) and aciertos != cantidadLetras: 
        esta = False 
        termino = False
        palabraAdivinada = ''.join (tablero) 
        print (palabraAdivinada) 
        
        
        letra = input ("Ingrese la letra: ")
        letra = letra.lower()
        
        listasUtilizadas.append (letra + " , ")
        if (len(listasUtilizadas) > 0):
            print ("Las letras que se usaron fueron: ")
            for i in range (len(listasUtilizadas)):
                print (listasUtilizadas[i],end = '')
        
        for i in range (len(palabra)-1):   
            if (palabra[i] == letra):
                tablero[i] = letra
                esta = True
            
        
        if (esta == True):
            print ("\nAcertaste la letra!")
            letrasRepetidas = palabra.count (letra)
            aciertos += letrasRepetidas
            usoIntentos += 1
            print('\n')
            dibujo = dibujaPersona (intentos)

        
        if (esta == False): #Aca esta el sumador de intentos
            intentos += 1
            restantes = chances - intentos
            print ("\n")
            dibujo = dibujaPersona (intentos)
            print ("Te quedan", restantes,'intentos')
        
    

    
    if (aciertos == cantidadLetras):
        print ("Adivinaste! la palabra era",palabra)
        listaPuntajes.append (usoIntentos)
    else: 
        print ("Perdiste... La palabra era", palabra) 
        listaPuntajes.append (0)

    


for i in range (len(listaPuntajes)):
    if (listaPuntajes[i] == 0):
        print ("El\la jugador\a ",listaParticipantes[i]," no adivino la palabra")
    else:
        print("El\la jugador\a", listaParticipantes[i]," adivino en: ", listaPuntajes[i], "intentos")