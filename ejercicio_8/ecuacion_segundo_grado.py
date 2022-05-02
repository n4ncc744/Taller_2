"""problema No.8: 
elaborar un programa que obtenga las raices de una ecuación de segundo grado """

print("-------------------------------------")
print("------LAS RAICES DE UNA ECUACIÓN ----")
print("-----------DE SEGUNDO GRADO----------")
import math

print("\n una ecuacion de segundo grado es de la forma ax^2+bx+c=0\n")
a = input("ingrese el valor de a:")
a = float(a)
b = input("ingrese el valor de b:")
b = float(b)
c = input("ingrese el valor de c:")
c = float(c)
d = float((b*b)-(4*(a)*(c)))

if d < 0:
    print("la ecuacion tiene solucion en los complejos")
elif d > 0:
    if a != 0:
        if b != 0:
            x1 = (-(b) + math.sqrt((b*b)-(4*(a)*(c)))) / (2*(a))
            x1 = float(x1)
            x2 = (-(b) - math.sqrt((b*b)-(4*(a)*(c))))/(2*(a)) 
            x2 = float(x2)
            print("x1 = "+str(x1))
            print("x2 = "+str(x2))
        else:
             print("la ecuacion tiene solo solucion en los numeros complejos")
    else:
        print("la ecuacion tiene solo solucion en los numeros complejos")
else:
    print("la ecuacion tiene solo solucion en los numeros complejos")