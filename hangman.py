import random
"""Creo que para el TP usamos archivos, y lo que fuimos viendo antes del primer parcial, no sé como incluiría tuplas, o diccionarios. Tuplas, podemos incluirlo como que el usuario ingrese su nombre y si adivina guardamos en una tupla el nombre del usuario y la cant de intentos, y después, comparamos todos los usuarios y vemos quien lo hizo en menos intentos
x ejemplo (juan, 5) lo comparamos con (gabriel, 2). Lo haria de dos niveles, el nivel facil, que te de la primer letra de la palabra elegida y mas chances , y el avanzado que no te de ninugna pista y tengas menos intentos """
def buscaPalabras (): #Cargamos un archivos con palabras y acá, la traemos al programa principal como lista
    arch = open ("palabras.txt", "rt")
    palabras = arch.readlines ()
    arch.close ()
    return palabras

def generaRenglones (a): #Genera la cantidad de _ que tiene la palabra, simplemente un detalle estético
    lista = []
    for i in range (len(a)-1):
        lista.append ("_") 
    return lista

def seleccionaPalabra (listaImportada): #Busca, aleatoriamente la palabra que será utilizada para que el usuario la adivine
    palabraAdivinar = listaImportada[random.randint(0,len(lista) - 1)] 
    return palabraAdivinar

lista = buscaPalabras ()
palabra = seleccionaPalabra (lista)
tablero = generaRenglones (palabra)
chances = 5
intentos = 0
print (palabra) #La dejo para ir probando si funciona el codigo, pero hay que sacar este print


while (chances > intentos): #Mientras no llegue a los 5 intentos, sigue pidiendole letras y llena el tablero (los rengoles) con las letras correctas que el usuario va poniendo
    esta = False 
    termino = False
    letra = input ("Ingrese la letra: ")
    for i in range (len(palabra)-1):
        if (palabra[i] == letra):
            print ("Acertaste...")
            tablero[i] = letra
            print (tablero)
            esta = True

    if palabra == str(tablero): #Esto todavia no lo pude hacer funcionar, que el algoritmo se de cuenta cuando se termina el juego si ganas
        print ("Ganaste")
        
    if (esta == False): #Aca esta el sumador de intentos
        intentos += 1 
    print (intentos)


print ("Perdiste... La palabra era", palabra) #Mensaje si el usuario pasa los intentos sin poder adivinar la palabra