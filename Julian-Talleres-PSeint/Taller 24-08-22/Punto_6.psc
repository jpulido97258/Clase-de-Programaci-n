Algoritmo Punto_6
	Dimension Lista(10)
	
	Escribir "Los multiplo de 5 hasta el 50 son:"
	Para i = 5 Hasta 50 Con Paso 5 Hacer
		Lista(i/5) = i
		Escribir Sin Saltar lista(i/5) ",";
	FinPara
	Escribir "."
	Escribir "Estos multiplos divididos entre 5 son igual a:"
	Para i = 1 Hasta 10 Con Paso 1 hacer	
		Lista(i) = Lista(i)/5
		Escribir Sin Saltar lista(i) ",";
	FinPara
	Escribir "."
FinAlgoritmo
