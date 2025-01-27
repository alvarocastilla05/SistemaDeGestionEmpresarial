def poner_mayuscula_a_palabras(cadena):
    resultado = ""
    siguiente_mayuscula = True 
    
    for caracter in cadena:
        if caracter.isalpha() and siguiente_mayuscula:
            resultado += caracter.upper()  
            siguiente_mayuscula = False
        else:
            resultado += caracter
        
        if not caracter.isalpha():
            siguiente_mayuscula = True
    
    return resultado

texto = "este es un ejemplo de texto!"
print(poner_mayuscula_a_palabras(texto)) 