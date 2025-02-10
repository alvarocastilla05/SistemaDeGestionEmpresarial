# Dado numbers = range(20), se genera una lista que contiene la palabra 
# "par" si un número en los números es par, y la palabra "impar" si el número es impar.
#  El resultado se vería así: "impar", "impar", "par".

numbers = range(20)

lista = ["par" if i % 2 == 0 else "impar" for i in numbers]
print(lista)
