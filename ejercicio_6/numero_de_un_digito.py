"""problema No.6: 
Determinar si resultado de sumar sus dos ultimos digitos es un número de un digito"""

print("----------------------------------------------------------------------")
print("-----la suma de los utimos dos digitos da como resultado un digito----")
print("----------------------------------------------------------------------")

# input 
x = int(input("ingrese el valor de un número: "))

# processign 

n1 = x % 10 
n2 = (x % 100)//10
n3 = n1 + n2

if 0 <= n3 < 10:
    msj = ("es de un 1 digito ")
else:
    msj = ("no es 1 digito")
# output

print(" la suma de los dos ultimos digitos de " + str(x) + msj)