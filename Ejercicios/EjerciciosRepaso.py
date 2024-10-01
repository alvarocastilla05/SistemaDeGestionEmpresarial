import math

#Ejercicio 1 --> Area de rectángulo

def area_rectangulo(base, altura) :
    
    return base * altura

print(area_rectangulo(15, 10))

#Ejercicio 2 --> Área de círculo

def area_circulo(radio) :
    return math.pi*radio**2

print(area_circulo(5))

#Ejercicio 3

def relacion(a, b) :
    if(a>b):
        return 1
    if(b>a) :
        return -1
    else :
        return 0
    
print(relacion(5, 10))
print(relacion(10, 5))
print(relacion(5, 5))

#Ejercicio 4

def intermedio(a, b) :
    return (a+b)/2

print(intermedio(-12, 24))


#Ejercicio 5

def recortar(numero, minimo, maximo) :
    if(numero < minimo):
        return minimo
    if(numero > maximo) :
        return maximo
    else :
        return numero
    
print(recortar(15, 0, 10))

#Ejercicio 6

def separar(lista) :
    
    pares = []
    impares = []

    for numero in lista  :
        if(numero%2 == 0) :
            pares.append(numero)
        else :
            impares.append(numero)

    return pares, impares

pares, impares = separar([6,5,2,1,7])
print(pares)
print(impares)


