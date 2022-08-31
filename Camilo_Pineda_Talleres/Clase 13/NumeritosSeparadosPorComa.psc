Algoritmo numeritos
	// Aqui defino la variable largo.
	Definir largo Como Entero;
	// aqui asigno el valor del largo
	largo <- 50;
	
	// aqui creo el arreglo numbers con la cantidad de espacios de largo
	Dimension numbers[largo];
	
	// Aqui creo un ciclo de tipo for que se repetira 50 veces
	Para i <- 1 Hasta largo Hacer
		numbers[i] <- i // para el espacio con valor i se asignara el valor de i
		Escribir numbers[i], ", " Sin Saltar; // aqui escribo el numero asignado en numbers para el valor de i y lo separo con una coma.
	FinPara
	
FinAlgoritmo
