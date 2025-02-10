### File Handing ###

# .txt file

txt_file = open("intermedio/my_file.txt", "r+") #Leer y escribir
#print(txt_file.read())
#print(txt_file.read(10))
#print(txt_file.readline())

for line in txt_file.readlines():
    print(line)


txt_file.write("\nHola")
print(txt_file.readline())

# .json file

import json

json_file = open("intermedio/my_file.json", "w+")

json_test = {"Nombre": "Alvaro", "Apellido": "Castilla", "Edad": 19}


