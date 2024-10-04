import csv
from datetime import datetime
from math import sqrt
from collections import namedtuple

#1-Definimos el objetos en la siguiente linea. Primer parametro nombre del namedtuple y luego sus atributos.
Avistamiento = namedtuple('Avistamiento', 'fechahora, ciudad, estado, forma, duracion, comentario, latitud, longitud')

#2-Función de lectura que crea una lista de avistamientos
def lee_avistamientos(fichero):
    res = []
    #3-Creamos una variable llamada f que es donde abrimos el fichero.
    with open(fichero, encoding = 'utf-8') as f :   
        lector = csv.reader(f)
        next(lector)
        for x in lector :
            #Indicamos en que posición se encuentra cada atributo, además, todo lo que no sean string hay que castearlo.
            fecha_hora = x[0]
            fechahora = datetime.strptime(fecha_hora, '%m/%d/%Y %H:%M')
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

