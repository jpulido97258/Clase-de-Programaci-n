#Funcion masa corporal

import math

peso = float(input("Ingrese su peso corporal"))
estatura = float(input("Ingrese su estatura en metros"))
IMC = round(peso/math.pow (estatura,2),1)

print("Su IMC es de "+str(IMC))

lista = [["Composicion Corporal" "Indice masa corporal (IMC)"]["Peso inferior"]]
