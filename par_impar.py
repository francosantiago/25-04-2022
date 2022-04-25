"""PROGRAMA
PAR Y IMPAR"""

print("-------------------------------------")
print("--Saber si un numero es par o impar--")
print("-------------------------------------")

# input

x = int(input(" Ingrese el valor de x: "))

# processing

if x % 2 == 0:
    msj = "es par "

else:
    msj = "es impar "

# output

print(" el numero " + msj)