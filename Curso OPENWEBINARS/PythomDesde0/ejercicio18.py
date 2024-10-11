# Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.

nombre = input("Introduzca nombre: ")
apellido1 = input("Introduzca primer apellido: ")
apellido2 = input("Introduzca segundo apellido: ")

inicial = (nombre[0] + apellido1[0] + apellido2[0]).upper()

print("Sus iniciales son %s" % inicial)



