Algoritmo MultiplosCinco
	
	Dimension Multi[50] // aqui defino el arreglo Multi con 50 espacios
	
	Escribir "Los multiplos de 5 que hay entre 1 y 50 son: "
	
	Para i <- 1 Hasta 50 Hacer
		// aqui el codigo se repite hasta que i sea 50:
		Si i mod 5 == 0 Entonces // aqui se coprueba si son multiplos de 5, si lo son al dividirlo entre 5 su residuo es 0.
				Multi[i] <- i;
				Escribir Multi[i] , ", " Sin Saltar
		FinSi
	FinPara
	
	Escribir "" //Este escribir vacio es para tener en otra linea de la consola el proximo mensaje
	Escribir "Los multiplos 5 divididos en 5 son: "
	
	// aqui replico el codigo anterior, solo que ahora didivido entre 5 los multiplos.
	Para i <- 1 Hasta 50 Hacer
		Si i mod 5 == 0 Entonces
			Multi[i] <- i/5;
			Escribir Multi[i] , ", " Sin Saltar
		FinSi
	FinPara
	
	
FinAlgoritmo
