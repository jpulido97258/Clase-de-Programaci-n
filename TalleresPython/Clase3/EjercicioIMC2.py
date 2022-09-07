import math


peso = float(input("Ingrese su peso en kg: "));
estatura = float(input("Ingrese su estatura en centimetros: "))/100;

imc = round(peso/math.pow(estatura,2));

print("Su indice de masa corporal es de:", imc);
