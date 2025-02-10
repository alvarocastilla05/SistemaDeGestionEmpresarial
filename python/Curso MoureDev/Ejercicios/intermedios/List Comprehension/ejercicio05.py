# Obtén el índice y el valor como una tupla para los elementos de la lista 
# “hi”, 4, 8.99, 'apple', ('t,b','n'). El resultado se vería así (índice, valor), (índice, valor)

lista = ["hi", 4, 8.99, "apple", ("t,b", "n")]
resultado = [(i, v) for i, v in enumerate(lista)]
print(resultado)