# Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica. 
# Python3 no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿Cómo se puede calcular?

import math

num = float(input("Introduzca el número al que desea de hacerle la raíz cuadrada y cúbica"))

cuadrada = math.sqrt(num)
cubica = num**(1/3)

print("La raiz cuadrada de %.2f es %.2f y la raíz cúbica es %.2f" % (num, cuadrada, cubica))

