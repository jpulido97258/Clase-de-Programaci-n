Algoritmo Ejercicio_5
	Escribir "numeros"
	Dimension lista[5]
	lista[1] = 17
	lista[2] = 56
	lista[3] = 46
	lista[4] = 69
	lista[5] = 210
	Para i = 1 Hasta 5 Hacer
		Escribir lista[i]
	FinPara
	suma = 0
	Para i = 1 Hasta 5 Hacer
		suma = suma + lista[i]
		operacion<- suma/5
	FinPara
	Escribir "Promedio de estos numeros"
	Escribir operacion
FinAlgoritmo