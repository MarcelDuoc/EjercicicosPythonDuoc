import FuncionesDetalles as fn
#from FuncionesDetalles import sumar
 
#linea ppal
fn.SumarDosNumeros()

res = fn.sumar(4,5)
print(res)

num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))
res = fn.sumar(num1,num2)
print("La suma es: ",res)