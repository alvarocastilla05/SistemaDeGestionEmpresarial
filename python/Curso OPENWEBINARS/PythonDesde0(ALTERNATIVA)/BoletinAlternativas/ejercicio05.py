# Escribe un programa que pida un nombre de usuario y una contraseña 
# y si se ha introducido "pepe" y "asdasd" se indica "Has entrado al sistema", 
# sino se da un error.

nombre = "pepe"
contrasenia = "asdasd"

usuario = input("Usuario: ")
contraseniaIntroducida = input("Contraseña: ")

if nombre == usuario and contrasenia == contraseniaIntroducida :
    print("Has entrado al sistema")
elif nombre != usuario :
    print("Nombre Incorrecto")
elif contrasenia != contraseniaIntroducida :
    print("Contraseña Incorrecta")
else :
    print("Usuario y Contraseña Incorrecta.")
