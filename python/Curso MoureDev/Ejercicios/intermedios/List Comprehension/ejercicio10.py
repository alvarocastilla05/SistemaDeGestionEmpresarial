# Encuentra todas las palabras en una cadena que tengan menos de 4 letras

cadena = input("Introduce una cadena de texto: ")

palabras_cortas = [palabra for palabra in cadena.split() if len(palabra) < 4]
print(palabras_cortas)