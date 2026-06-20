def mostrarMenu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar vehículo")
    print("2. Buscar vehículo")
    print("3. Eliminar vehículo")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar vehículos")
    print("6. Salir")
    print("=====================================")

def solicitarOpcion():
    while True:
        try:
            opcion = int(input("Ingrese la opción a realizar: "))
            if opcion >= 1 and opcion <= 6 :
                return opcion
            else:
                print("Ingrese una opción válida de menú (1-6)")
        except ValueError:
            print("Ingrese una opción válida de menú")

def validaModelo(modelo):
    if modelo.strip() == "":
        return False
    else:
        return True
    
def validaAnio(anio):
    try:
        anioNumerico = int(anio)

        if anioNumerico < 1900:
            return False
        else:
            return True
    except ValueError:
        return False

def validaPrecio(precio):
    try:
        precioDecimal = float(precio)
        if precioDecimal > 0:
            return True
        else:
            return False    
    except ValueError:
        return False


    

def agregarVehiculo(listaVehiculos):
    modelo = input("Ingresa el modelo del vehiculo (sin espacios): ")
    anio = input("ingresa el año de fabricación del vehiculo (mayor a 1900): ")
    precio = input("Ingresa el precio del vehiculo (mayoe a 0): ")

    modeloValido = validaModelo(modelo)
    anioValido= validaAnio(anio)
    precioValido = validaPrecio(precio)

    if modeloValido and anioValido and precioValido:
        vehiculo = {
            "modelo": modelo,
            "anio": int(anio),
            "precio": float(precio),
            "disponible": False
        }

        listaVehiculos.append(vehiculo)
        print("Vehiculo agregado correctamente")
    else:
        print("Los datos no cumplen con los valores correctos")

def buscarVehiculo(lista, modelo):

    # for vehiculo in lista:
    #     if modelo == vehiculo["modelo"]:
    #         return lista.index(vehiculo)

    for posicion, vehiculo in enumerate(lista):
        if modelo == vehiculo["modelo"]:
            return posicion
        
    return -1

def actualizarDisponibilidad(lista):

    for vehiculo in lista:
        if vehiculo["anio"] >= 2020:
            vehiculo["disponible"] = True
        else:
            vehiculo["disponible"] = False
    
def mostrarTodosVehiculos (lista_vehiculos):
    actualizarDisponibilidad (lista_vehiculos)

    print("=== LISTA DE VEHICULOS ===")
    
    if len(lista_vehiculos) == 0:
        print("No hay vehículos registrados en el concesionario.")
        print("********************************************")
    else:
        for vehiculo in lista_vehiculos:
            if vehiculo["disponible"]:
                estado_texto = "DISPONIBLE"
            else:
                estado_texto = "NO DISPONIBLE"
                
            print(f"Modelo: {vehiculo['modelo']}")
            print(f"Año: {vehiculo['anio']}")
            print(f"Precio: {vehiculo['precio']}")
            print(f"Estado: {estado_texto}")
            print("********************************************")

#Codigo PPal

listadoVehiculosAlmacenados = []

while True:

    mostrarMenu()

    opcionseleccionada = solicitarOpcion()

    match opcionseleccionada:

        case 1:
            agregarVehiculo(listadoVehiculosAlmacenados)
        case 2:
            modeloBuscado =input("Ingresa el modelo a buscar: ")

            posicionVehiculo = buscarVehiculo(listadoVehiculosAlmacenados, modeloBuscado)

            if posicionVehiculo >= 0:
                print(listadoVehiculosAlmacenados[posicionVehiculo])
            else:
                print(f"El vehículo {modeloBuscado} no se encuentra registrado.")

        case 3:
            modeloBuscado =input("Ingresa el modelo a buscar: ")

            posicionVehiculo = buscarVehiculo(listadoVehiculosAlmacenados, modeloBuscado)

            if posicionVehiculo >= 0:
                listadoVehiculosAlmacenados.pop(posicionVehiculo)
            else:
                print(f"El vehículo {modeloBuscado} no se encuentra registrado.")

        case 4:
           actualizarDisponibilidad(listadoVehiculosAlmacenados)

        case 5:
            mostrarTodosVehiculos(listadoVehiculosAlmacenados)

        case 6:
            print("Gracias por usar el sistema. Vuelva Pronto")
            break

    

#time 2:11 Finish