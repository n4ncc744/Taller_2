"""problema No.5: 
verificar si un nùmero entero tiene sus dos ultimos digitos iguales"""

print("----------------------------------------------")
print("------LOS DOS ULTIMOS DIGITOS SON IGUALES?----")
print("----------------------------------------------")

# input 
número =int(input("Digite el valor de el número: "))

# processign 
ultimo_digito = int(str(número)[-1])
penultimo_digito = int(str(número)[-2])

# output
if ultimo_digito == penultimo_digito:
    print("son iguales")
else:
    print("son dierentes")

