#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

import math

cateto1 = float(input("Indica cateto1: "))
cateto2 = float(input("Indica cateto2: "))

hipotenusa = math.sqrt(cateto1**2 + cateto2**2);

print("La hipotenusa es %.2f"%(hipotenusa))

