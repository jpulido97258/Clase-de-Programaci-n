Algoritmo Taller6_260822 //Generar un algortimo que nos muestre una lista de los multiplos del 5//
	//Pero solo numeros desde el 1 al 50//
	Escribir "Solo multiplos de 5"
	Escribir "Digite numers del 1 al 50"
	Dimension Lista(50)
	Para i=1 Hasta 50 hacer
		Lista(i) = i
	FinPara
	Para J=5 Hasta 50 Con Paso 5 Hacer
		Escribir Lista(J)
	FinPara
	//Lista(Rta)<-Lista(J)/5 //Comentar error
	//Escribir (Lista(J)/5) //Para imprimir la division era necesario de un comando "for"
	Escribir "Ahora se deviden por 5"
	Para J=5 Hasta 50 con paso 5 Hacer
		Escribir (Lista(J)/5)
	FinPara
	
FinAlgoritmo
