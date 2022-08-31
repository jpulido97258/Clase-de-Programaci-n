Algoritmo Mutliplosde3
	
	Definir largo Como Entero //aqui defino el largo
	largo <- 100; //aqui defino que el largo es 100.
	
	Dimension num[largo] //aqui defino el arreglo num con la cantidad de spacios de largo.
	
	Escribir "Los multiplos de 3 que estan en el arreglo son: "
	
	Para i <- 1 Hasta largo Hacer //aqui repito el ciclo para hata que llenen todos los espacios del arreglo
		num[i] <- i; //aqui asigno a la posicion i del arreglo num el numero de i
		
		Si num[i] mod 3 == 0 Entonces // aqui verifico si son multiplos de 3
			Escribir num[i] , ", "  Sin Saltar; //si son multiplos de 3 los escribo en la pantalla.
		FinSi
		
	FinPara
	
FinAlgoritmo
