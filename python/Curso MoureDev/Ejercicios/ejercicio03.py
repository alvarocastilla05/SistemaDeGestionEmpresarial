cadena1=input("Dime una palabra:")
cadena2=input("Dime otra:")

print(cadena1[0])
print(cadena1[1])



def comporacion(cadena1, cadena2):

    distinto1 = ""
    distinto2 = ""

    for letra1 in cadena1:
        if letra1 not in cadena2:
            distinto1 += letra1

    for letra2 in cadena2:
        if letra2 not in cadena1:
            distinto2 += letra2

    print("Caracteres en cadena1 pero no en cadena2:", distinto1)
    print("Caracteres en cadena2 pero no en cadena1:", distinto2)
                
comporacion(cadena1, cadena2)