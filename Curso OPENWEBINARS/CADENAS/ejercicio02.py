#Realizar un programa que compruebe si una cadena leida por teclado 
#comienza por una subcadena introducida por teclado

cad = input("Introduzca una cadena: ")
subcad = input("Introduzca subcadena: ")

if cad.startswith(subcad) :
    print("La cadena comienza por la subcadena")
else :
    print("La cadena no comienza por la subcadena")