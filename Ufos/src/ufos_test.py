from ufos import *

import csv
from datetime import datetime
from math import sqrt
from collections import namedtuple

# Test de la función lee_avistamientos

Avistamiento = namedtuple('Avistamiento', 'fechahora, ciudad, estado, forma, duracion, comentario, latitud, longitud')

def lee_avistamientos(fichero):
    res = []
    with open(fichero, encoding = 'utf-8') as f :
        lector = csv.reader(f)
        for x in lector :
            fecha_hora = x[0]
            fechahora = datetime.strptime(fecha_hora, "%m/%d/%Y %H:%M")
            ciudad = x[1]
            estado = x[2]
            forma = x[3]
            duracion = int(x[4])
            comentarios = x[5]
            latitud = float(x[6])
            longitud = float(x[7])
            tupla = Avistamiento(fechahora, ciudad, estado, forma, duracion, comentarios, latitud, longitud)
            res.append(tupla)
    
    return res



# with open("ovnis.csv", newline="\n") as csvfile:
#     reader = csv.DictReader(csvfile)
#      for ovni in reader :
#          print(ovni["fechahora"], ovni["ciudad"], ovni["estado"], ovni["forma"], ovni["duracion"], ovni["comentarios"], ovni["latitud"], ovni["longitud"])

#Test de la función duracion_total

    
# Test de la función comentario_mas_largo



# Test de la función avistamientos_fechas



# Test de la función hora_mas_avistamientos









