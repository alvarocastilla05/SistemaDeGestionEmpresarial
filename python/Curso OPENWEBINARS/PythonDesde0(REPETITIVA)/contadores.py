#Un contador es una variable entera que la utilizamos para contar cuando
#ocurre un suceso.


#Ejemplo1 --> contador de número introducidos pares.
cont = 0
for var in range(1,6) :
    num = int(input("Dime un número: "))
    if num % 2 == 0 :
        cont = cont + 1
print("Has introducido %d números pares" % cont)

#El acumulador es una variable numérica que permite ir acumulando operaciones.
#Me permite ir haciendo operaciones parciales.

suma = 0
for var in range(1,6) :
    num2 = int(input("Dime un número: "))
    if num % 2 == 0:
        suma = suma + num2
print("La suma de los números pares es %d" % suma)