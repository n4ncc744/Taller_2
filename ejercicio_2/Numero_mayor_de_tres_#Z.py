"""Ejercicio No.2:
Dados tres números enteros, determinar cuál de ellos es el mayor"""

print("---------------------------------------------------")
print("------NÚMERO MAYOR DE TRES NÚMEROS ENTEROS:--------")
print("---------------------------------------------------")

# input 
x = int(input("Digite el valor de un número entero: "))
y = int(input("Digite el valor de un número entero: "))
z = int(input("Digite el valor de un número entero: "))

# processign 
if x > y and x > z:
    print("el número entero mayor",x)
elif y > x and y > z:
    print("el número entero mayor",y)
elif z > x and z > y:
    print("el número entero mayor",z)
else:
     print("no se pudo establecer el mayor")