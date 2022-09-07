#vriable  mu,ti funcion 

import math 

peso = float(input ("ingrese su peso corporal")) # ingresa un valor numerico en kilogramos
estatura = float (input ("ingrese su estatura en metros")) #ingrese un valor numerico en decimales/centumetros

imc =round (peso/math.pow(estatura,2),1) #formula para sacear la potencia del peso y 

print("su imc es de"+str (imc)) # Me muesra el resultado en cadena de texto 
lista = [["composicion corpotal ", "indie de masa corporal (imc) "]]
