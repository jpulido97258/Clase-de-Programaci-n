#Hacer una funcion que calcule la masa corporal
import math

#Ingresa un valor numerico en kilogramos
peso = float(input("ingrese su peso corporal: "))
#Ingresa un valor numerico en 
estatura = float(input("ingrese su estatura en metros: "))
#Formula para sacar la potencia de el peso y 
imc = round(peso/math.pow (estatura,2),1)
#Imprime la cadena de texto imc
print("Su imc es de " + str(imc))
lista = [["Composicion corporal", "Indice de masa corporal (imc)"], ["Peso inferior al no"]]