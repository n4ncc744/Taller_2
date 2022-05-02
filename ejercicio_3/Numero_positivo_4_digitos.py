"""Ejercicio No.3:
Construir un programa que lea un número entero y saber si es un número positivo de 4 digitos"""


print("------------------------------------------------")
print("------NÚMERO POSITIVO DE 4 DIGITOS--------------")
print("------------------------------------------------")

# input 
x = int(input("Digite el valor de un número entero: "))

# processign
if 999 < x < 10000:
    msj = ("es de cuatro digitos" )
else:
    msj = (" no tiene cuatro digitos")

# output

print("\nel número " + str(x) + msj)

