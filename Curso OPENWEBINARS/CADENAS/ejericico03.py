#Pide una cadena y carácter por teclado 
#(válida que sea una carácter) y muestra cuantas veces
#aparece el carácter en la cadena

cad = input("Introduzca una cadena: ")

while True :
    car = input("Introduce un carácter: ")
    if len(car)>1:
        print("Me tienes que dar un solo caracter")

    if len(car) == 1: break

print("En la cadena", cad, "aparecen ", cad.count(car), "veces el carácter" )