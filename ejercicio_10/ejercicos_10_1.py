"""Ejercicio No.10:
Dados 3 números los devuelva en orden ascendente"""

print("---------------------------------------------------")
print("-------dados 3 números los devuelva en ------------")
print("----------------orden ascendente-------------------")

print("digite el primer numero:")
num1 = int(input()) 
print("digite el segundo numero:")
num2 = int(input()) 
print("digite el tercero numero:")
num3 = int(input()) 

if(num1>num2 and num2>num3):
    print("",num1," - ",num2," - ",num3)
elif (num2>num1 and num2>num3):
    print("",num2," - ",num1," - ",num3)
elif (num3>num1 and num1>num2):
    print("",num3," - ",num1," - ",num2)
elif (num3>num2 and num2>num1):
    print("",num3," - ",num2," - ",num1)
elif (num1>num3 and num3>num2):
    print("",num1," - ",num3," - ",num2)
elif (num2>num3 and num3 >num1):
    print("",num2," - ",num3," - ",num1)

else: 
    print("se ingresaron números iguales")


