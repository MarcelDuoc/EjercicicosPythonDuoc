'''productos = {
    "Mouse": [10, 15000],
    "Teclado": [5, 25000],
    "Monitor": [3, 180000]
}'''

#productos = [] Lista

def agregar_productos(productos):
    nombre

# codigo ppal

productos = {} #diccionario vacío

while True:
    print ("------- MENU -------")
    print ("1. Agregar producto")
    print ("2. Mostrar productos")
    print ("3. Buscar productos")
    print ("4. Producto mas caro")
    print ("5. Salir")
    print ("*********************")

    while True:
        try:
            op = int(input("Ingrese la opción: +"))
            break
        except ValueError:
            print ("Debe ingresar una opción válidad (1-5, intente nuevamente)")

    if op == 1:
        print ("Agregar Producto")

    elif op == 2:
        print ("Mostrar Productos")

    elif op == 3:
        print ("Buscar Productos")

    elif op ==4:
        print ("Producto más caro")

    elif op ==5:
        print ("Fin del programa")
        break
    
    else:
        print ("Opción no válida")


    