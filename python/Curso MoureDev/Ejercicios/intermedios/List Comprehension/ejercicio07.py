# Obtén solamente los números en una oración como 'En 1984 hubo 13 casos de protesta con más de 1000 asistentes'


cadena = "En 1984 hubo 13 casos de protesta con más de 1000 asistentes"

numeros = [int(palabra) for palabra in cadena.split() if palabra.isdigit()]

print(numeros)