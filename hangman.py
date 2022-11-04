import random
"""Creo que para el TP usamos archivos, y lo que fuimos viendo antes del primer parcial, no sé como incluiría tuplas, o diccionarios. Tuplas, podemos incluirlo como que el usuario ingrese su nombre y si adivina guardamos en una tupla el nombre del usuario y la cant de intentos, y después, comparamos todos los usuarios y vemos quien lo hizo en menos intentos
x ejemplo (juan, 5) lo comparamos con (gabriel, 2)"""
def buscaPalabras (): #Cargamos un archivos con palabras y acá, la traemos al programa principal como lista
    arch = open ("palabras.txt", "rt")
    palabras = arch.readlines ()
    arch.close ()
    return palabras

def generaRenglones (a): #Genera la cantidad de _ que tiene la palabra, simplemente un detalle estético
   for i in range (len(a)):
    print ("_", end=" ")

def seleccionaPalabra (listaImportada): #Busca, aleatoriamente la palabra que será utilizada para que el usuario la adivine
    palabraAdivinar = listaImportada[random.randint(0,len(lista) - 1)] 
    print (palabraAdivinar)
    return palabraAdivinar

lista = buscaPalabras ()
palabra = seleccionaPalabra (lista)
guiones = generaRenglones (palabra)

chances = 5
intentos = 0
while (intentos < chances):
    intentos += 1
    palabraAdivinar = list(palabra)
    print (palabraAdivinar)
    letra = input ("Ingrese una letra: ")
    for i in range (len(palabraAdivinar)):
        if letra == palabraAdivinar[i]:
            print ("Correcto! La letra", letra, "esta en la posicion", palabraAdivinar[i+1])
        else:
            print ("Letra incorrecta")
        letra = input ("Ingrese una letra: ")
