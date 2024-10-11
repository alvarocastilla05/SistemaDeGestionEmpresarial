# Dadas dos variables numéricas A y B, que el usuario debe teclear, 
# se pide realizar un algoritmo que intercambie los valores de ambas variables 
# y muestre cuanto valen al final las dos variables.


a = int(input("Introduzca valor de A: "))
b = int(input("Introduzca valor de B: "))

aux = a 
a = b
b = aux

print("A = %d" % a)
print("B = %d" % b)

