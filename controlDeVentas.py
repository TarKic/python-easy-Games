def cantidadDeProductos ():
    cantidad = int (input ("Ingrese la cantidad de productos que tiene para vender: "))
    m = [[0 for j in range(cantidad)] for i in range(3)]
    for i in range (3):
        for j in range (cantidad):
            if (i == 0):
                nombreProducto = str(input ("Ingrese el nombre del producto: "))
                m [i][j] = nombreProducto
            elif (i == 1):
                print ("Carga Stock del producto", m[0][j])
                cantidad = int (input ("Ingrese la cantidad:")) 
                m[i][j] = cantidad
            elif (i == 2):
                print ("Cargara el precio UNITARIO del producto", m[0][j])
                precioUnitario = int (input("Ingrese el precio: "))
                m[i][j] = precioUnitario

    for i in range (3):
        print ()
        for j in range (cantidad):
            print ("%3a"%m[i][j], end= " ")
    return (m)


def cargaVentas (mat):
    print (len(mat))


matrizProductos = cantidadDeProductos ()
matrizPostVentas = cargaVentas (matrizProductos)