# Escribir un algoritmo para calcular la nota final de un estudiante, considerando que: 
# por cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en 
# blanco 0. Imprime el resultado obtenido por el estudiante.

correctas = int(input("Introduzca el número de respuestas correctas: "))
incorrectas = int(input("Introduzca el número de respuestas incorrectas: "))

puntuacionFinal = (correctas*5) - incorrectas

print("Su puntuación final es %d" % puntuacionFinal)
