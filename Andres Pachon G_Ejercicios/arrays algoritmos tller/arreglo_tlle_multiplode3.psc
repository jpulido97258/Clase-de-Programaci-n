Algoritmo arreglo_tlle_multiplode3
	//definicion de la variable
	Definir T Como Entero
	
	T<-100
	Dimension Largo[T]
	para i=1 Hasta T Hacer
		si i MOD 3 = 0 Entonces
			Largo[i]<- i
			Escribir Largo[i], ";" Sin Saltar // se hace este sin saltar para que la impresion sea mas comoda
		FinSi
		
	FinPara
FinAlgoritmo
