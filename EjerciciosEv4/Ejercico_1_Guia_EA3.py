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
    if nombre.isdigit():
        print("El nombre no puede ser un digito")
        return
    
    while True:
            try:
                stock = int(input("Ingrese Stock: "))
                if stock >= 0:
                    break
                else:
                    print("El stock debe ser mayor o igual a 0")
            except ValueError:
                print("El Stock, debe ser un número entero mayor o igual a 0")
    while True:
        try:
            precio = int(input("Ingrese precio $: "))
            if precio >0:
                break
            else:
                print("El precio debe ser mayor que 0")
        except ValueError:
            print("El Precio, debe un número entero mayor que 0")

    productos [nombre] = [stock,precio]
    print ("Producto agregado correctamente!")

def mostrar_productos(productos):
    if len(productos) == 0:
        print("No existen productos")
        return
    for nombre in productos:
        print(nombre,"-Stock: ",productos[nombre][0],"-Precio: $",productos[nombre][1])

def buscar_productos(productos):
    if len(productos) == 0:
        print("No existen productos")
        return
    nombre = input("Ingrese nombre del producyo a buscar: ").strip().lower()

    if nombre in productos:
        print(f"Producto {nombre} encontrado")
        print(f"Stock: {productos[nombre][0]}")
        print(f"Precio: {productos[nombre][1]}") 

    else:
        print("Producto no existe o esta agotado")
        
def producto_mas_caro(productos):
    if len(productos) == 0:
        print("No existen productos")
        return
    
    mayor = 0
    nombreMayor = ""
    for nombre in productos:
        precio = productos [nombre][1]

        if precio > mayor:
            mayor = precio
            nombreMayor = nombre

    print(f"producto mas caro es: {nombreMayor}")
    print(f"Su precio es: ${mayor}")

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
        # for Key,Value in productos.items():
        #     print (Key,Value)
        print ("Buscar Productos")
        buscar_productos(productos)
    elif op ==4:
        #print ("Producto más caro")
        producto_mas_caro(productos)
    elif op ==5:
        print ("Fin del programa")
        break
    
    else:
        print ("Opción no válida")

