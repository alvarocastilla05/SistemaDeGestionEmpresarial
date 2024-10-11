# Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos 
# en el plano. Calcula y muestra la distancia entre ellos.

print("Dime las coordenadas del punto 1")

x1 = int(input("x1:"))
y1 = int(input("y1:"))

print("Dime las coordenadas del punto 2")

x2 = int(input("x2:"))
y2 = int(input("y2:"))

diferenciaX = x1-x2
diferenciaY = y1-y2

print("La diferencia entre el punto 1 y punto 2 es: (%d, %d)" % (diferenciaX, diferenciaY))