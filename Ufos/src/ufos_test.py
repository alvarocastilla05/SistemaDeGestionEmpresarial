from ufos import *

# Test de la función lee_avistamientos
avistamientos = lee_avistamientos("Ufos\data\ovnis.csv")

for a in avistamientos[:5]:
    print(a)




#Test de la función duracion_total

print(duracion_total(avistamientos, 'in'))
print(duracion_total(avistamientos, 'nm'))
print(duracion_total(avistamientos, 'pa'))
print(duracion_total(avistamientos, 'wa'))

    
# Test de la función comentario_mas_largo
  





# Test de la función avistamientos_fechas



# Test de la función hora_mas_avistamientos









