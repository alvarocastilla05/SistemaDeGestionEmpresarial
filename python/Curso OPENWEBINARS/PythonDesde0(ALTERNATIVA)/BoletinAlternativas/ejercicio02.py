#Algoritmo que pida un número por teclado y diga si es positivo, negativo o 0.

num = int(input("Introduzca un número: "))

if num < 0 :
    print("El número es negativo.")
elif num > 0 :
    print("El número es positivo.")
else :
    print("El número es igual a 0.")