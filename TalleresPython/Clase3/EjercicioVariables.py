#Este es un ejercicio de variables.
import math

#Este programa va a encontrar los posibles valores para x en una cuacion cuadratica

#aqui solicito los valores de A,B,C que se voy a usar para la formula cuadratica
a = float(input("Ingresa el valor de A: "));
b = float(input("Ingresa el valor de B: "));
c = float(input("Ingresa el valor de C: "));

#aqui guardo en diferentes variables el resultado al sumar la raiz y al restar la raiz
resPos = (-b + math.pow((b**2)-(4*a*c), 1/2)) / (2*a);
resNeg = (-b - math.pow((b**2)-(4*a*c), 1/2)) / (2*a);

#aqui imprimo los dos posibles resultados para x
print("El resultado sumando la raiz es: X =" , resPos);
print("El resultado restando la raiz es: X =" , resNeg);