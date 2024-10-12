#Realizar un algoritmo que muestre la tabla de multiplicador de un número 
#introducido por teclado

tabla = int(input("Introduzca la tabla que desea: "))

for num in range(1, 11) :
    print("%d * %d = %d" % (num, tabla, num*tabla))