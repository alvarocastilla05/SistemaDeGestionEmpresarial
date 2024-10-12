# Escribe un programa que diga si un número introducido por teclado es o no primo. 
# Un número primo es aquel que sólo es divisible entre él mismo y la unidad. 
# Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es 
# divisible por algún otro número.

es_primo = True
numPrimo = int(input("Introduzca un número para ver si es primo: "))

for num in range(2, numPrimo) :
    if numPrimo % num == 0 :
        es_primo = False
        break
if es_primo :
    print("Es primo")
else :
    print("No es primo")