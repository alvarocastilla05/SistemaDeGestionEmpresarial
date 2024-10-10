#Un alumno desea saber cual será su calificación final en la materia
#Dicha calificación se compone de los siguiente porcentajes:
# * 55€ del promedio de sus tres calificaciones parciales.
# * 30% de la calificación del examen final.
# * 15% de la calificación de un trabajo final.

parcial1 = float(input("Indique nota del primer parcial: "))
parcial2 = float(input("Indique nota del segundo parcial: "))
parcial3 = float(input("Indique nota del tercer parcial: "))

promedio = (parcial1+parcial2+parcial3)/3

puntosPromedio = promedio*0.55

examenFinal = float(input("Indique nota del examen final: "))

puntosExamaen = examenFinal*0.3

trabajoFinal = float(input("Indique nota del trabajo final: "))

puntosTrabajo = trabajoFinal*0.15

notaFinal = puntosPromedio+puntosExamaen+puntosTrabajo

print("La nota media de sus parciales es %.2f" % promedio)
print("La nota de su examen final es %.2f" % examenFinal)
print("La nota del trabajo final es %.2f" % trabajoFinal)

print("Por lo tanto su nota final es %.2f" % notaFinal)


