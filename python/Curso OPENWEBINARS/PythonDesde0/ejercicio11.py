# Pide al usuario dos números y muestra la "distancia" entre ellos 
# (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).

num1 = float(input("Introduzca número 1: "))
num2 = float(input("Introduzca número 2: "))

diferencia = num1 - num2

print("El valor absoluto de la diferencia de los números anteriores es: %.2f" % abs(diferencia))


