# Realizar variable multifuncion

from cgi import print_arguments


peso = float(input("Ingrese su peso en kg: "))
altura = float (input("Ingrese su estatura en metros: "))

imc = round (peso/(altura**2))

print("El imc es de" +str(imc))

lista = [["Composición corporal","indice de masa corporal (imc)"],["Peso muy bajo, menos de 18.5"],["Peso normal, entre 18.5 y 24.9"],["Sobrepeso, entre 25 y 29.9"],["Obesidad, imc mayor que 30"]]

if imc<18.5:
    print("Peso muy bajo, menos de 18.5")
elif imc>=18.5 & imc<=24.9:
     print("Peso normal, entre 18.5 y 24.9")
elif imc>=25 & imc<=29.9:
    print("Sobrepeso, entre 25 y 29.9")
elif imc>=30:
    print("Obesidad, imc mayor que 30")