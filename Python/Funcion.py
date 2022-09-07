#Variable, multifuncion
import math #para poder realizar potencias
peso = float (input('Ingrese su peso corporal')) #float para definir entero
estatura = float (input('Ingrese su estatura en metros'))
IMC = round (peso/math.pow (estatura ,2),1) #dos valores
print ('su IMC es de ', str(IMC))


