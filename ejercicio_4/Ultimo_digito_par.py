"""problema No.4: 
verificar si un nùmero entero tiene el ultimo  digito de un 
numero par """

print("----------------------------")
print("------ULTIMO DIGITO PAR?----")
print("----------------------------")

# input 
x = int(input("Digite el valor de un número entero x: "))

# processign 
ultimo_digito = x % 10 
r = ultimo_digito % 2

if r == 0:
    print("El ultimo digito de " + str(x) + "es PAR")
if r!= 0:
    print("El ultimo digito de " + str(x) + "es IMPAR")