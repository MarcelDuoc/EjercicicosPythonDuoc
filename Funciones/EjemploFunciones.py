#funciones

def SumarDosNumeros():
    '''Esta funcion permite dumar dos números,
    ingresados dentro de la función
    '''

    num1= int(input("Ingrese número 1: "))
    num2= int(input("Ingrese número 2: "))

    suma = num1 + num2

    print(f"la suma de {num1} + {num2} es = {suma}")

def sumar(a,b):
    '''Esta función permite sumar dos números
    ingresados por parámetros
    '''

    suma = a + b
    return suma

#linea ppal
SumarDosNumeros()

res = sumar(4,5)
print(res)

num1 = int(inout("Numero 1: "))
num2 = int(inout("Numero 2: "))
res = sumar(num1,num2)
print("La suma es: ",res)