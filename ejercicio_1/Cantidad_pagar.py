"""Ejercicio No.1:
Verificar la cantidad a pagar de una llamada telefonica"""


print("-------------------------------------------")
print("------VALOR A PAGAR DE UNA LLAMADA:--------")
print("-------------------------------------------")

# input 
T=int(input("Digite el valor del tiempo en minutos: "))

# processign 
if T <= 3:
    print("El valor de la llamada es $300");
elif T > 3:
    M = int((T - 3))
    p = (300 + M * 50)
    print("El total a pagar por minutos de la llamada es: " + str(p))