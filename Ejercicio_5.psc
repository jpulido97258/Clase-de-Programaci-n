Algoritmo Ejercicio_5
	Escribir "Lista de numeros"
	//proceso lista
	Dimension lista[8]
	lista[1] = 63
	lista[2] = 45
	lista[3] = 68
	lista[4] = 96
	lista[5] = 110
	lista[6] = 203
	lista[7] = 10
	lista[8] = 8
	Para i = 1 Hasta 8 Hacer
		Escribir lista[i]
	FinPara
	suma = 0
	Para i = 1 Hasta 8 Hacer
		suma = suma + lista[i]
		operacion<- suma/8
	FinPara
	Escribir "Promedio de estos numeros"
	Escribir operacion
FinAlgoritmo
