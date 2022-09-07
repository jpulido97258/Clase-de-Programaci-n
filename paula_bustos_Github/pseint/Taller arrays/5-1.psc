//En un array con los datos 63, 45, 68, 96,110,203,10,8 escribe
//un programa que los promedie e imprima por pantalla el resultado
Algoritmo punto_5
	Dimension lista[8]
	lista[1] = 63
	lista[2] = 45
	lista[3] = 68
	lista[4] = 96
	lista[5] = 110
	lista[6] = 203
	lista[7] = 10
	lista[8] = 8
	para i = 1 hasta 8 Hacer
		Escribir  lista[i]
	FinPara
	
	suma = 0
	para i = 1 hasta 8 Hacer
		suma = suma + lista[i]
	FinPara
	Escribir suma
FinAlgoritmo