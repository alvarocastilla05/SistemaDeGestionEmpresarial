def calcular_ganador(jugadas):

    puntuacion_jugador1= 0
    puntuacion_jugador2= 0

    reglas = {
        "R" : "S",
        "S" : "P",
        "P" : "R"
    }

    for p1, p2 in jugadas:
        if p1 == p2:
            continue
        elif reglas[p1] == p2:
            puntuacion_jugador1 += 1
        else:
            puntuacion_jugador2 += 1


    
    if puntuacion_jugador1 > puntuacion_jugador2:
        return "Player 1 gana"
    elif puntuacion_jugador2 > puntuacion_jugador1:
        return "Player 2 gana"
    else: 
        return "Empate"
    

jugadas = [("R", "S"), ("S", "R"), ("P", "S")]
resultado = calcular_ganador(jugadas)
print(resultado) 
