# Dado un número de dos cifras, diseñe un algoritmo que permita obtener el 
# número invertido.

num = int(input("Introduzca un número de 2 cifras"))

if num < 10 or num > 99:
    print("El número introducido no es de dos cifras")
else:
    decenas = num // 10
    unidades = num % 10

    print("El número invertido es: %d%d" % (unidades, decenas))
    

