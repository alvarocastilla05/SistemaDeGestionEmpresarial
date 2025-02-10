#El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35 con las siguientes columnas: Nombre (nombre de la empresa), Final (precio de la acción al cierre de bolsa), Máximo (precio máximo de la acción durante la jornada), Mínimo (precio mínimo de la acción durante la jornada), Volumen (Volumen al cierre de bolsa), Efectivo (capitalización al cierre en miles de euros).

#Construir una función reciba el fichero de cotizaciones y devuelva un diccionario con los datos del fichero por columnas.
#Construir una función que reciba el diccionario devuelto por la función anterior y cree un fichero en formato csv con el mínimo, el máximo y la media de dada columna.

import csv

def leer_fichero():
    cotizaciones = []
    with open("./Ficheros/cotizacion.csv", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            if all(key in row for key in ["Nombre", "Final", "Máximo", "Mínimo", "Volumen", "Efectivo"]):
                cotizacion = {
                    "nombre": row["Nombre"],
                    "final": float(row["Final"].replace('.', '').replace(',', '.')),
                    "maximo": float(row["Máximo"].replace('.', '').replace(',', '.')),
                    "minimo": float(row["Mínimo"].replace('.', '').replace(',', '.')),
                    "volumen": float(row["Volumen"].replace('.', '').replace(',', '.')),
                    "efectivo": float(row["Efectivo"].replace('.', '').replace(',', '.'))
                }
                cotizaciones.append(cotizacion)
            else:
                print(f"Fila con datos faltantes: {row}")
    print(f"Cotizaciones leídas: {cotizaciones}")  
    return cotizaciones

def cotizaciones_por_columnas(cotizaciones):
    columnas = {"final": [], "maximo": [], "minimo": [], "volumen": [], "efectivo": []}
    for cotizacion in cotizaciones:
        for key in columnas.keys():
            columnas[key].append(cotizacion[key])
    print(f"Datos por columnas: {columnas}")  
    return columnas

def crear_fichero_cotizaciones_por_columnas(columnas):
    with open("./Ficheros/cotizaciones_por_columnas.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Columna", "Mínimo", "Máximo", "Media"])
        for key in columnas.keys():
            if columnas[key]:  
                writer.writerow([key, min(columnas[key]), max(columnas[key]), sum(columnas[key]) / len(columnas[key])])
            else:
                print(f"La columna {key} está vacía y no se puede calcular el mínimo, máximo y media.") 

def menu():
    cotizaciones = leer_fichero()
    columnas = cotizaciones_por_columnas(cotizaciones)
    crear_fichero_cotizaciones_por_columnas(columnas)

menu()