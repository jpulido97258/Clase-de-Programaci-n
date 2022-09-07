# Variable multifunción

import math

peso = float (input ("Ingrese su peso corporal:")) # Ingreso de peso en kilogramos
estatura = float (input ("Ingrese su estatura en metros:")) #Ingresar estatura en metros

IMC = round(peso/math.pow (estatura,2,1)) #Resultado en cadena de texto IMC 

print ("Su indice de masa corporal es de:",str(IMC))

lista = [["Composición corporal","Indice de masa corporal (IMC)"]["Peso Inferior al normal"]]
