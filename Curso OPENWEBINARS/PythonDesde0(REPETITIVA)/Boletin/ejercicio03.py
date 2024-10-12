#Algoritmo que pida números hasta que se introduzca un cero. Debe de imprimir la suma
#y la media de todos los números introducidos.

suma = 0
cont = 0

num = int(input("Introduzca un número (0 para salir): "))

while num != 0 :
    suma = suma + num
    cont = cont + 1
    num = int(input("Introduzca un número (0 para Salir): "))

#Si cont=0 no puedo realizar la división de la media.
if cont > 0 :
    media = suma / cont
else:
    media = 0

print("Suma: ", suma)
print("Media: ", media)
