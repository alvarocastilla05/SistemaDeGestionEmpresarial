secreto = "asdasd"
while True :
    clave = input("Dime la clave: ")
    if clave != secreto :
        print("Clave Incorrecta!")
    if clave == secreto :
        break
print("Bienvenido")