//Crea un arreglo con los múltiplos de 5 que hay desde el 1 hasta el 50 (10),
//luego divide cada posición del arreglo en 5
Algoritmo punto_6
	Dimension lista[10]
	para i = 5 hasta 50 con paso 5 Hacer
		lista[i/5] = i
	FinPara
	para i = 1 hasta 10 con paso 1 Hacer
		lista[i] = lista[i]/5
		Escribir lista(i)
	FinPara
FinAlgoritmo