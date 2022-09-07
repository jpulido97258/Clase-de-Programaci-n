Algoritmo Ejercicio_5
	Escribir "Escribir un numero entero positivo a restar"
	Definir num1 Como Entero
	leer num1
	Si num1 < 0 Entonces
		Escribir "El numero que pusiste es negativo, por lo tanto pasara a ser positivo y se entregara una resta"
		resta2 <- num1 * (-1)
		resta3 <- resta2 - 1
		Escribir "El resultado de la resta es: ", resta3;
	SiNo
		resta <- num1 -1
		Escribir "El resultado de la resta es: ", resta;
	Fin si
	Escribir  "Escribir los numeros a dividir"
	Definir num2 Como Entero
	Definir  num3 Como Entero
	Leer num2
	Leer num3
	Division <- num2/num3
	Escribir  "El resultado de la division es: ", Division;
FinAlgoritmo
//Division y resta