"""Ejercicio No.9:
determinar el monto de descuento o el monto del recargo y el total a pagar"""

print("---------------------------------------------------")
print("-------monto de descuento y el total a pagar-------")
print("---------------------------------------------------")

x = float(input("ingresa el monto de la compra: "))
y = float(input("cliente general o cliente afliado: "))
z = float(input("pago de contado o pago a plazos "))

if y == "cliente general" and z == "pago de contado":
    w = x * 0.15
    T = (x - w)
    print("el monto de la compra es $" + str(x) + ", el monto de decuento o recarga es $" + str(w) + 
    " y el total a pagar es $" + str(T));

elif y == "cliente general" and z == "pago a plazos":
    w = x * 0.1
    T = (x + w)
    print("el monto de la compra es $" + str(x) + " , el monto del descuento o recargo de $" + str(w) +
    " y el total a pagar es $" + str(T));

elif y == "cliente afiliado" and z == "pago de contado":
    w = x * 0.2
    T = (x - w)
    print("el monto de la compra es $" + str(x) + " , el monto del descuento o recargo de $" + str(w) +
    " y el total a pagar es $" + str(T));

elif y == "cliente afiliado" and z == "pago a plazos":
    w = x * 0.05
    T = (x + w)
    print("el monto de la compra es $" + str(x) + " , el monto del descuento o recargo de $" + str(w) +
    " y el total a pagar es $" + str(T));

else:
    print("Rectifique la información.");
