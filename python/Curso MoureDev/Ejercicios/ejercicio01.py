diccionario={
    'A':'._', 'B':'_...', 'C':'_._.', 'D':'_..', 'E':'.', 'F':'.._.', 'G':'__.',
    'H':'....', 'I':'..', 'J':'.___', 'K':'_._', 'L':'._..', 'M':'__', 'N':'_.',
    'O':'___', 'P':'.__.', 'Q':'__._', 'R':'._.', 'S':'...', 'T':'_', 'U':'.._',
    'V':'..._', 'W':'.__', 'X':'_.._', 'Y':'_.__', 'Z':'__..','0':'_____','1':'.____',
    '2':'..___','3':'...__','4':'...._','5':'.....','6':'_....','7':'__...','8':'___..','9':'____.', " ":" "
}

diccionario2 = {
    '._': 'A', '_...': 'B', '_._.': 'C', '_..': 'D', '.': 'E', '.._.': 'F', '__.': 'G',
    '....': 'H', '..': 'I', '.___': 'J', '_._': 'K', '._..': 'L', '__': 'M', '_.': 'N',
    '___': 'O', '.__.': 'P', '__._': 'Q', '._.': 'R', '...': 'S', '_': 'T', '.._': 'U',
    '..._': 'V', '.__': 'W', '_.._': 'X', '_.__': 'Y', '__..': 'Z', '_____': '0', '.____': '1',
    '..___': '2', '...__': '3', '...._': '4', '.....': '5', '_....': '6', '__...': '7',
    '___..': '8', '____.': '9', " ": " "
}

a_traducir = input("Introduzca la palabra a traducir: ")


if a_traducir.startswith(".") or a_traducir.startswith("_"):
    
    array = []

    a_traducir = a_traducir.split(" ")

    for binario in a_traducir:

        array.append(diccionario2[binario])

    print("Traduccion a texto: ", ''.join(array))

    print(array)
else :
    array = []

    for normal in a_traducir.upper():
        
        array.append(diccionario[normal])

    print("Traducción a morse: ", ' '.join(array))