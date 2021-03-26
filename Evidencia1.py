ventas = {}

def registroVentas():
    respuesta = 1
    while respuesta == 1:
        claveCompra = int(input("Ingresa una clave de compra: "))
        try:
            if claveCompra in ventas:
                print ("ESA CLAVE YA ESTA REGISTRADA INTENTE CON OTRA")
                claveCompra = int(input("Ingresa una clave de compra: "))
        finally:
            print ("CLAVE ACEPTADA")
                        
        descripcionArticulo = input("¿Cual es la descripción del articulo?: ")
        cantidadPiezasVendidas = int(input("¿Cual es la cantidad de piezas vendidas?: "))
        precioDeVenta = int(input("¿Cual es el precio de venta?: "))
        ventas[claveCompra] = [descripcionArticulo,cantidadPiezasVendidas,precioDeVenta]
        total = cantidadPiezasVendidas * precioDeVenta
        print (f"Su total de compra seria de: {total}")
        respuesta = int(input("¿DESEA REGISTRAR OTRA VENTA?: 1-.SI/2-.NO: "))

def consulta():
    buscarVenta =int(input("Dime la clave de compra de la venta realizada: "))
    if buscarVenta in ventas.keys():
        print(ventas[buscarVenta])
    else:
        print("la clave que ingreso no existe")