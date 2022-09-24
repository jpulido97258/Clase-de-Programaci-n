Algoritmo Ejercicio_6
	Escribir "Multiplos de 7 hasta el 67:"
	Dimension lista[10]
	Para i = 7 Hasta 67 Con Paso 7 Hacer
		lista[i/7] = i
		Escribir Sin Saltar "," lista[i/7]
	FinPara
	Escribir "."
	Escribir "Dividido en 5 posiciones:"
	Para i = 1 Hasta 10 Con Paso 1 Hacer
		lista[i] = lista [i]/7
		Escribir lista(i)
	FinPara
FinAlgoritmo