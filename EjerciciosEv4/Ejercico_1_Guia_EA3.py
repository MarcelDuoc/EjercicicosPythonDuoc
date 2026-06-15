'''productos = {
    "Mouse": [10, 15000],
    "Teclado": [5, 25000],
    "Monitor": [3, 180000]
}'''

def agregar_productos(productos):
    nombre = input("Nombre del producto: ").strip().lower()

    if nombre == "":
        print("El nombre no puede ser vacío")
        return
    if nombre in productos:
        print("El producto ya existe!")
        return
    
    stock = int(input("Ingrese Stock: "))
    precio = int(input("Ingrese precio $: "))

    productos [nombre] = [stock,precio]
    print ("Producto agregado correctamente!")

def mostrar_productos(productos):
    if len(productos) == 0:
        print("No existen productos")
        return
    for nombre in productos:
        print(nombre,"-Stock: ",productos[nombre][0],"-Precio: $",productos[nombre][1])

#def buscar_productos(productos):
#def producto_mas_caro(productos):

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
            op = int(input("Ingrese la opción: "))
            break
        except ValueError:
            print ("Debe ingresar una opción válidad (1-5, intente nuevamente)")

    if op == 1:
        print ("Agregar Producto")
        agregar_productos(productos)

    elif op == 2:
        print ("Mostrar Productos")
        mostrar_productos(productos)
    elif op == 3:
        print ("Buscar Productos")
        #buscar_productos(productos):
    elif op ==4:
        print ("Producto más caro")
        #producto_mas_caro(producto):
    elif op ==5:
        print ("Fin del programa")
        break
    
    else:
        print ("Opción no válida")

