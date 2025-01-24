# Realizar un algoritmo que pida números (se pedir� por teclado la cantidad de 
# números a introducir). El programa debe informar de cuantos números introducidos 
# son mayores que 0, menores que 0 e iguales a 0.

cantidad = int(input("Cuántos números va a introducir?"))

mayor0 = 0
menor0 = 0
ceros = 0

for i in range(1, cantidad+1) :
    print("Número ",i,":",end="")
    num = int(input())

    if num < 0 :
        menor0 = menor0 + 1
    elif num > 0 :
        mayor0 = mayor0 + 1
    else :
        ceros = ceros + 1

print("Positivos : %d" % mayor0) 
print("Negativos: %d" % menor0)
print("Ceros: %d" % ceros)