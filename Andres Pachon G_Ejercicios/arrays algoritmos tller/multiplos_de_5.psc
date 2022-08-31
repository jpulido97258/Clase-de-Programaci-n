Algoritmo multiplos_de_5
	//hacer un for para que se muestren nada mas los numeros multiplos de 5 del 1 al 50
	t<- 50
	Dimension Largo[T]
	para i=1 Hasta T Hacer
		si i MOD 5 = 0 Entonces
			Largo[i]<- i
			Escribir Largo[i]
		FinSi
	FinPara
	
	Escribir "ahora cada uno de los valores seran divididos en 5"
	// se toma el mismo concepto de antes pero ahora eso se divide en 5
	Para i=1 Hasta T Hacer
		si i MOD 5 = 0 Entonces
			Largo[i]<- i/5
			Escribir Largo[i]
		FinSi
	FinPara
	
FinAlgoritmo
