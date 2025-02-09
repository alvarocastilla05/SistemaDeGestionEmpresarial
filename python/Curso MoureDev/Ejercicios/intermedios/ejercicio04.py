#Crea una lista de todas las consonantes de la cadena “A los yaks amarillos 
# les gusta gritar y bostezar y ayer cantaban mientras comían ñames asquerosos”


cadena = "A los yaks amarillos les gusta gritar y bostezar y ayer cantaban mientras comían ñames asquerosos"
vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
consonantes = [c for c in cadena if c.isalpha() and c not in vocales]
print(consonantes)


