# Suponiendo que hemos introducido una cadena por teclado que representa una frase 
# (palabras separadas por espacios), realiza un programa que cuente cuantas 
# palabras tiene.

cont = 0
posicion = 0

cad = input("Introduzca una cadena: ")

#Eliminamos los posibles espacios del principio y final (strip())
cad = cad.strip()
#Buscamos los espacios 
posicion = cad.find(" ", posicion)
while posicion != -1 :
    cont = cont + 1
    #No tengo en cuenta los posibles espacios que haya entre palabras
    while cad[posicion + 1] == " ":
        posicion = posicion + 1
    posicion = cad.find(" ", posicion + 1)
print("La frase tiene", cont + 1, "palabras.")