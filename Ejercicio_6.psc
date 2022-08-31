Algoritmo Ejercicio_6
	Escribir "Multiplos de 5 hasta el 50:"
	//lista multiplos de 5 hasta el 50
	Dimension lista[10]
	Para i = 5 Hasta 50 Con Paso 5 Hacer
		lista[i/5] = i
		Escribir Sin Saltar "," lista[i/5]
	FinPara
	Escribir "."
	Escribir "Dividido en 5 posiciones:"
	//division en 5 
	Para i = 1 Hasta 10 Con Paso 1 Hacer
		lista[i] = lista [i]/5
		Escribir lista(i)
	FinPara
FinAlgoritmo
