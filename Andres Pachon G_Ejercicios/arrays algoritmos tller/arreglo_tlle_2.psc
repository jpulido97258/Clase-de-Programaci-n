Algoritmo arreglo_tlle_2
	//definir variable
	Definir T Como Entero
	// pedir una cantidad de giros para realizar el procedimiento
	Escribir "Escriba cuantos giros quieres dar a la ruleta"
	Leer T
	
	Dimension ruleta[T]
	
	Para i=1 Hasta T Hacer
		ruleta[i] = azar(1000)
		Escribir ruleta[i]
	FinPara
	
FinAlgoritmo
