secreto = "asdasd"
clave = input("Dime la clave: ")
while clave != secreto :
    print("Clave Incorrecta!")
    otra = input("¿Quieres introducir otra clave (S/N)? ")
    if otra.upper() == "N" :
        break
    clave = input("Dime la clave: ")
if clave == secreto :
    print("Bienvenid@")