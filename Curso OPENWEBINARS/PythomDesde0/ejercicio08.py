# Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, 
# el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por 
# las tres ventas que realiza en el mes y el total que recibirá en el mes tomando 
# en cuenta su sueldo base y comisiones.

precioSillas = float(input("Indica el precio de venta de las 3 sillas vendidas: "))
comisionVentas = (precioSillas*3)*0.10

sueldoBase = float(input("Indique su sueldo base: "))

sueldoTotal = sueldoBase + comisionVentas

print("Obtiene una comisión de ventas de %.2f € y su sueldo total es de %.2f €" % (comisionVentas, sueldoTotal))