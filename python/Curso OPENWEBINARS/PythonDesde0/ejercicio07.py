# Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a 
# cuantas horas y minutos corresponde.

min = float(input("Introduzca una cantidad de minutos: "))

horas = min / 60
minRes = min % 60

print("%.2f min son un total de %.2f horas y %.2f mins" % (min, horas, minRes))
