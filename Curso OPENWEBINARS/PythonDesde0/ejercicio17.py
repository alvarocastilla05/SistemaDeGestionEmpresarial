# Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. 
# El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. 
# Escribir un algoritmo que determine la hora de llegada a la ciudad B.

horaSalida = int(input("Hora salida: "))
minSalida = int(input("Minuto salida: "))
segSalida = int(input("Segundo salida: "))
segViaje = int(input("Tiempo que ha durado el viaje en segundos: "))

#Convierto la hora de salida a segundos

segInicial = (horaSalida*3600)+(minSalida*60)+segSalida

segFinal = segInicial+segViaje

#Convierto el total de segundos a hora, min y seg
horaLlegada = segFinal//3600 #División entera
minLlegada = (segFinal % 3600) // 60
segLlegada = (segFinal % 3600) % 60

#Muestro la hora de llegada
print("La hora de llegada es %d:%d:%d" % (horaLlegada, minLlegada, segLlegada))