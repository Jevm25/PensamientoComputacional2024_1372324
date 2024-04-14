print("Bienvenidos, porfavor seleccione una opciòn")
distancias = {(51, 61): 39, (51, 71): 18, (71, 82): 23, (61, 51): 8, (82, 51): 42}
menu = ['1.Ver las estaciones existentes', '2.Comprar boleto', '3.Reportes', '4.Salir']
estaciones = ['Código             Nombre de Estación','51                   Estación Javier', '61                   Estación Trébol', '71                   Estación Don Bosco', '82                   Estación Plaza Municipal']
rutas = ['Estacion de salida        Estacion de destino        Distancia(km)', '51        61         39km', '51        71         18km', '71        82         23km', '61        51         08km', '82        51         42km' ]
opcion = 100

ventas_registradas = []

while opcion != '4':
    if opcion == '0,0':
        break

    for lista in menu:
        print('\n'+lista)

    #menu
    print("Ingrese numero de opciòn")
    opcion = str(input())

    match opcion:
        case '1':
            print("Ingresando a ver las estaciones existentes...")
            print("...")
            print("...")
            print("Estaciones")
            for list in estaciones:
                print('\n'+list)
            for list in rutas:
                print('\n'+list)

        case '2':
            print("Ingresando a comprar boletos")
            print("...")
            print("...")
            ruta = (100,100)
            while ruta != (0,0):
                print("Ingrese la estacion de salida")
                while True:
                    try:
                        partida = int(input())
                        break
                    except ValueError:
                        print("No cuenta, porfavor coloque uno valido")
                print("Ingrese la estacion de destino")
                while True:
                    try:
                        destino = int(input())
                        break
                    except ValueError:
                        print("No cuenta, porfavor coloque uno valido")
                ruta = (partida,destino)

                if ruta == (0,0):
                    break
                if (ruta == (51,61) or ruta == (51,71) or ruta == (71,82) or ruta == (61,51) or ruta == (82,51)) or ruta == (0,0):
                    print("Esta ruta"+ str(ruta) + "Existe!continuemos...")
                    print("Ingrese su nombre completo")
                    nombre = input()
                    while True:
                        try:
                            edad = int(input("Ingrese su edad: "))
                            break
                        except ValueError:
                            print("Por favor, ingrese solo números para la edad.")
                    distancia = distancias[ruta]
                    primeros = distancia - 8
                    print("La distancia son: " + str(distancia) +'km')
                    print("Los primeros 8km son a Q1.50 y cada km adicional son Q0.25")
                    precio = 1.50 * 8 + 0.25 * (distancia - 8)
                    print("Indique si se encuentra embarazada Si/No")
                    respuesta = input()
                    tiempo = distancia/20
                    estaciones = {51: 'Estación Javier', 61: 'Estación Trébol', 71: 'Estación Don Bosco', 82: 'Estación Plaza Municipal'}
                    
                    if respuesta == 'si':
                        print("Su boleto es gratis")
                        embarazada = precio - precio
                        informaciones = ['Esta es su información a nombre de: '+ nombre, 'Ruta a tomar: '+ estaciones[ruta[0]] + ' - ' + estaciones[ruta[1]], 'Precio a pagar: Q'+str(embarazada) + ' Su boleto es gratis', 'Tiempo del viaje: ' + str(tiempo) +'horas']
                        for info in informaciones:
                            print('\n'+info)
                    else:
                        informaciones = []
                        for i in range(15, 26):
                            if i == edad:
                                descuento = precio * 0.25
                                precio_final = precio - descuento
                                print("Usted tiene un descuento del 25% por ser estudiante <3")
                                informaciones = ['Esta es su información a nombre de: '+ nombre, 'Ruta a tomar: '+ estaciones[ruta[0]] + ' - ' + estaciones[ruta[1]], 'Precio a pagar con descuento: Q'+ str(precio_final), 'Tiempo del viaje: ' + str(tiempo) +' horas']
                                break
                        if not informaciones:
                            informaciones = ['Esta es su información a nombre de: '+ nombre, 'Ruta a tomar: '+ estaciones[ruta[0]] + ' - ' + estaciones[ruta[1]], 'Precio a pagar: Q'+str(precio), 'Tiempo del viaje: ' + str(tiempo) +' horas']
                    for info in informaciones:
                        print('\n'+info)
                    while True:
                        try:
                            confirmar = (input("Escribir CONFIRMAR, para confirmar compra: "))
                            break
                        except ValueError:
                            print("Escriba correctamente CONFIRMAR")
                    con = input()
                    con = 0
                    confirmar = con + 1
                    ventas_registradas.append((ruta, precio))

                else:
                    print("Esta ruta"+ str(ruta) + "No existe!! coloca ruta existente")
                print("Para salir ingrese 0,0")

        case '3':
            print("Ingresando a los Reportes")
            print("...")
            print("...")
    
            boletos_vendidos_por_ruta = {ruta: 0 for ruta in distancias}
            total_dinero_percibido = 0

            for venta in ventas_registradas:
                ruta, precio = venta
                boletos_vendidos_por_ruta[ruta] += 1
                total_dinero_percibido += precio
            print("Reporte de cantidad de boletos vendidos por ruta:")
            for ruta, cantidad in boletos_vendidos_por_ruta.items():
                print(f"Ruta {ruta}: {cantidad} boletos vendidos")

            print("\nTotal de dinero percibido por la venta de boletos: Q", total_dinero_percibido)

        case '4':
            print("Finalizado")

        case _:
            print("Porfavor, elejir una opciòn valida :)")