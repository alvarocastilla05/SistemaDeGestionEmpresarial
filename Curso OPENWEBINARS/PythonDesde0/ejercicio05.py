# Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.

fahrenheit = float(input("Introduzca grados fahrenheit: "))

celsius = (fahrenheit - 32) * 5 / 9

print("%.2f graos Fahrenheit es igual a %.2f grados Celsius" % (fahrenheit, celsius))