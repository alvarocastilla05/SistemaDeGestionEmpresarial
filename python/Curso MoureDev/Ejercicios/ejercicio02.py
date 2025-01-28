
def esta_equilibrado(expresion):
    pares = {"(": ")", "[": "]", "{": "}"}
    delimitadores = []  

    for caracter in expresion:
        if caracter in pares.keys():  
            delimitadores.append(caracter) 
        elif caracter in pares.values(): 
           
            if not delimitadores or pares[delimitadores.pop()] != caracter:
                return False

    
    return not delimitadores


# Ejemplo
expresion = "{ [ a * ( c + d ) ] - 5 }"
expresion2= " { a * ( c + d ) ] - 5 }"
print(esta_equilibrado(expresion))  
print(esta_equilibrado(expresion2))  
