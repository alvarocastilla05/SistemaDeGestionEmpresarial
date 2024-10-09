# Calcular el perímetro y área de un rectángulo dada su base y su altura.

base = float(input("Indique base: "))
altura = float(input("Indique altura: "))

perimetro = base*2 + altura*2
area = base*altura

print("El perimetro del rectángulo es %.2f m y el área es %.2f m2" % (perimetro, area))