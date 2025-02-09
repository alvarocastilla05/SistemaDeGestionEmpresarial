# Utiliza una comprensión de lista anidada para encontrar todos los 
# números del 1 al 1000 que sean divisibles por cualquier dígito excepto 1 (2-9)

numeros_divisibles = [num for num in range(1, 1001) if any(num % d == 0 for d in range(2, 10))]
print(numeros_divisibles)
