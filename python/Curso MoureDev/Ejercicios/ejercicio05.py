def evaluar_carrera(acciones, pista):
    pista_modificada = ""
    superado_correctamente = True

    for i in range(len(pista)):
        if pista[i] == "_" and acciones[i] == "run":
            pista_modificada += "_"  
        elif pista[i] == "|" and acciones[i] == "jump":
            pista_modificada += "|"  
        elif pista[i] == "_" and acciones[i] == "jump":
            pista_modificada += "x"  
            superado_correctamente = False
        elif pista[i] == "|" and acciones[i] == "run":
            pista_modificada += "/"  
            superado_correctamente = False

    print(pista_modificada)
    return superado_correctamente

acciones = ["run", "jump", "run", "jump", "jump"]
pista = "_|__|"
resultado = evaluar_carrera(acciones, pista)
print("¿Ha superado la carrera correctamente?", resultado)