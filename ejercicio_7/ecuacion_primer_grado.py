"""Ejercicio No.7:
Elaborar un programa para resolver una ecuación de primer grado"""


print("--------------------------------------------")
print("------ECUACIÓN DE PRIMER GRADO--------------")
print("--------------------------------------------")

a = int(input("ingresar el valor de a: "))
b = int(input("ingresar el valor de b: "))

if(a != 0):
    x = (-1*b) / a;
    print("solución de ecuaciones: "+ str(x))

elif(b != 0):
    print("solución imposible");

else:
    print("solución indeterminada");