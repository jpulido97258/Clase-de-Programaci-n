Algoritmo promedio_tllr
		//asignacion de la lista
	Dimension Lista[8]
	Lista[1]= 63
	Lista[2]= 45
	Lista[3]= 68
	lista[4]= 96
	lista[5]= 110
	lista[6]= 203
	lista[7]= 10
	lista[8]= 8
	// suma de cada parte de la lista para posteriormente dividir esta sumatoria en 8
	Definir x Como Entero
	x<- lista[1]+lista[2]+lista[3]+lista[4]+lista[5]+lista[6]+lista[7]+lista[8]
	Definir rta Como real
	rta<- x/8
	
	Escribir "El resultado del promedio es: ", rta
	
FinAlgoritmo
