def calcular_batalla(bondadosos, malvados):
    valores_bondadosos = {"Pelosos": 1, "Sureños buenos": 2, "Enanos": 3, "Númenóreanos": 4, "Elfos": 5}
    valores_malvados = {"Sureños malos": 2, "Orcos": 2, "Goblins": 2, "Huargos": 3, "Trolls": 5}

    poder_bondadosos = sum(valores_bondadosos[raza] * cantidad for raza, cantidad in bondadosos.items())
    poder_malvados = sum(valores_malvados[raza] * cantidad for raza, cantidad in malvados.items())

    if poder_bondadosos > poder_malvados:
        return "¡El bien triunfa sobre el mal!"
    elif poder_bondadosos < poder_malvados:
        return "¡El mal reina en la Tierra Media!"
    else:
        return "La batalla termina en empate."


bondadosos = {
    "Pelosos": 3,
    "Elfos": 1
}

malvados = {
    "Orcos": 1,
    "Trolls": 1
}

resultado = calcular_batalla(bondadosos, malvados)
print(resultado)
