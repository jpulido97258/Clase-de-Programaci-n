#Ejercicio IMC

import math

peso=float(input("ingrese su peso corporal: "))
estatura=float(input("ingrese su estatura en metros: "))

IMC=round(peso/math.pow(estatura,2),1)

print("Su IMC es de"+str(IMC))

lista=[["composicion corporal "]]