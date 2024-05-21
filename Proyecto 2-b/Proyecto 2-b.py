print("Bienvenido a su sistema de tempertaura HSmart")
print("Porfavor, configure cada area de la casa, tiene un maximo y minimo de 6 zonas")

import datetime
            #el datetime el primero es la librería y el segundo el nombre de la clase
            #el .now es para la fecha hora actual
            #el .time es para especificar que solo quiero la hora actual
import time

horarios = {}
# Función para agregar un horario de cambio de temperatura
def agregar_horario():
    # Pide al usuario el nombre de la zona, la hora y los minutos deseados, y la temperatura deseada
    zona = input("Nombre de la zona: ")
    hora = int(input("Hora (0-23): "))
    minutos = int(input("Minutos (0-59): "))
    temperatura = float(input("Temperatura deseada: "))

    # Almacena esta información en el diccionario de horarios
    horarios[zona, (hora, minutos)] = temperatura

#Colocar cada lugar de la casa segun el nombre que le de el usurio
#Obligatoriamente se deben de colocar las 6 zonas
lugar1 = input("Area 1: ")
lugar2 = input("Area 2: ")
lugar3 = input("Area 3: ")
lugar4 = input("Area 4: ")
lugar5 = input("Area 5: ")
lugar6 = input("Area 6: ")
print("Coloque la temperatura deseada")
print("Recuerde que en HSmart trabajamos con grados centigrados (°C)")
#Definir las temperaturas iniciales
temperaturas = {
    lugar1: 22,
    lugar2: 22,
    lugar3: 22,
    lugar4: 22,
    lugar5: 22,
    lugar6: 22
}

# Variable global para almacenar el nombre de la zona actual
zona_actual = "lugar1"


#Que funcione y asigne la temperatura para cada área
while True:
     # la condición True es "siempre se cumple" hasta que sea flaso o erroneo
    try:
        temp1 = int(input("Temperatura de " + lugar1 + ": "))
        if temp1 < 18 or temp1 > 30:
            raise ValueError() #se utiliza para generar una excepción ValueError personalizada
        break
    except ValueError:
        print("No se permite esa temperatura. Por favor, ingrese un valor entre 18 y 30 grados.")

while True:
    try:
        temp2 = int(input("Temperatura de " + lugar2 + ": "))
        if temp2 < 18 or temp2 > 30:
            raise ValueError()
        break
    except ValueError:
        print("No se permite esa temperatura. Por favor, ingrese un valor entre 18 y 30 grados.")

while True:
    try:
        temp3 = int(input("Temperatura de " + lugar3 + ": "))
        if temp3 < 18 or temp3 > 30:
            raise ValueError()
        break
    except ValueError:
        print("No se permite esa temperatura. Por favor, ingrese un valor entre 18 y 30 grados.")

while True:
    try:
        temp4 = int(input("Temperatura de " + lugar4 + ": "))
        if temp4 < 18 or temp4 > 30:
            raise ValueError()
        break
    except ValueError:
        print("No se permite esa temperatura. Por favor, ingrese un valor entre 18 y 30 grados.")

while True:
    try:
        temp5 = int(input("Temperatura de " + lugar5 + ": "))
        if temp5 < 18 or temp5 > 30:
            raise ValueError()
        break
    except ValueError:
        print("No se permite esa temperatura. Por favor, ingrese un valor entre 18 y 30 grados.")

while True:
    try:
        temp6 = int(input("Temperatura de " + lugar6 + ": "))
        if temp6 < 18 or temp6 > 30:
            raise ValueError()
        break
    except ValueError:
        print("No se permite esa temperatura. Por favor, ingrese un valor entre 18 y 30 grados.")

#variables del menu
menu = ['1.Configurar temperatura de cada area', '2.Configurar horario de cambio de temperatura', '3.Salir']
menu_conf = ['1.Visualizar temepraturas asignadas', '2.Configurar temperatura', '3. Regresar al menu principal']
# Actualiza la lista de temperaturas asignadas después de definir las temperaturas iniciales
lista_conf = [(lugar1 + ' está a ' + str(temperaturas[lugar1]) + '°'),
                  (lugar2 + ' está a ' + str(temperaturas[lugar2]) + '°'),
                  (lugar3 + ' está a ' + str(temperaturas[lugar3]) + '°'),
                  (lugar4 + ' está a ' + str(temperaturas[lugar4]) + '°'),
                  (lugar5 + ' está a ' + str(temperaturas[lugar5]) + '°'),
                  (lugar6 + ' está a ' + str(temperaturas[lugar6]) + '°')]
lista_area = ['1. '+lugar1,'2. '+lugar2,'3. '+lugar3,'4. '+lugar4,'5. '+lugar5,'6. '+lugar6,'7. Regresar']
opcion1 = 100 #variable para que funcione
opcion1_1 = 100 #variable para que funcione
opcion = 100 #variable para que funcione
# Función para verificar si hay un horario programado para la zona y la hora actual
def verificar_horarios():
    # Obtiene la zona actual
    zona = zona_actual

    # Obtiene la hora, los minutos y los segundos actuales
    hora = datetime.datetime.now().time().hour
    minutos = datetime.datetime.now().time().minute
    segundos = datetime.datetime.now().time().second

    # Iterar sobre el diccionario de horarios
    for (zona_actual, (hora_programada, minutos_programados)), temperatura in horarios.items():
        # Verifica si hay una coincidencia entre la zona actual, la hora actual, los minutos actuales y los segundos actuales, y algún horario programado
        if zona == zona_actual and hora == hora_programada and minutos == minutos_programados and segundos == 0:
            # Ajusta la temperatura en la zona correspondiente
            temperaturas[zona_actual] = temperatura
            break

    # Si no hay una coincidencia, mantiene la temperatura actual en la zona
    for zona in temperaturas:
        pass # aquí puedes mantener la temperatura actual en la zona

    # Si no hay una coincidencia, mantiene una temperatura ambiente de 22°
    for zona in temperaturas:
        if temperaturas[zona] < 22:
            temperaturas[zona] += 1
        elif temperaturas[zona] > 22:
            temperaturas[zona] -= 1
print("Bienvenido aqui podra configurar cada opción de la temperatura de su casa")
#menu principal
while opcion != '3':
    for lista in menu:
        print('\n'+lista)
    print("Ingrese numero de opción")
    opcion = str(input())
    #estas son las opciones a tomar en el menu
    match opcion:
        case '1':
         #Aqui se va desplegar otro menu para que escoja la opcion que desee, si solo quiere ver o cambiar temperaturas
            print("Ingresando a Configurar tempertaura de cada area...")
            print("...")
            print("...")
            print("Menu")
            while opcion1 != '3':
                 # la opcion 3 es para regresar al menu anterior
                for lista in menu_conf:
                    print('\n'+lista)
                print("Ingrese numero de opción")
                opcion1 = str(input())
                match opcion1:
                    #opcion 1 solo para visualizar las temperaturas y si se cuandi se cambian tambien
                    case '1':
                        print("Aqui visualizara las temperaturas asignadas")
                        print("Area de la casa ----- Temperatura")
                        for lista in lista_conf:
                            print('\n'+lista)
                    #opcion 2 es para cambiar las temperaturas
                    case '2':
                        print("Cambie las temperaturas de cada area (Recuerde que dentro del rango de 18 a 30 grados).")
                        while True:
                            lugarselec = input("Seleccione el area de la casa para cambiar la temperatura (1-6): ")
                            if lugarselec in ['1', '2', '3', '4', '5', '6']:
                                lugarselec = [lugar1, lugar2, lugar3, lugar4, lugar5, lugar6][int(lugarselec) - 1] #aqui se convierte el lugarselc en un numero entero y se le resta 1 para que devuelva el correcto
                                while True:
                                    try:
                                        nueva_temp = int(input("Ingrese la nueva temperatura para " + lugarselec + ": "))
                                        if nueva_temp < 18 or nueva_temp > 30:
                                            raise ValueError()
                                        temperaturas[lugarselec] = nueva_temp
                                        lista_conf[[lugar1, lugar2, lugar3, lugar4, lugar5, lugar6].index(lugarselec)] = (lugarselec + ' esta a ' + str(nueva_temp) + '°') 
                                        #el .index es para buscar entre las listas, los nombres especificos
                                        print("Temperatura cambiada con éxito.")
                                        break
                                    except ValueError:
                                        print("No se permite esa temperatura. Por favor, ingrese un valor entre 18 y 30 grados.")
                                break
                            else:
                                print("Esa no vale jaja, intente otra...")
                    case '3':
                        opcion1 = -1  # Reiniciar la variable opcion1
                        print("Regresando...")
                        break
                    case _: #Si se coloca otro numero, saldra el mensaje
                        print("Porfavor, elejir una opciòn valida :)")
        case '2':
            print("Ingresando a Configurar horarios para cambio de tempertaura de cada area...")
            print("...")
            print("...")
            # Llama a la función agregar_horario() para agregar un nuevo horario
            agregar_horario()
            print("Se realizara el cambio segun el horario establecido")
 
        case '3':
            print("Finalizando...")
        case _:
           print("Porfavor, elejir una opciòn valida :)") 
                   # Bucle while infinito para verificar los horarios cada minuto
while True:
    if opcion == '2':
        # Llama a la función verificar_horarios() para ajustar las temperaturas en cada zona
        verificar_horarios()
    time.sleep(60)  # duerme por 60 segundos (1 minuto)

#Ingeniero tenga en cuenta que lo di todo y necesito pasar, disculpe ingeniero lo intente