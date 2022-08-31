Algoritmo sextopunto 
	
	Escribir "Se colocaran los numeros del 1 al 50"
	Dimension Lista[10]
	para i=5 Hasta 50 Con Paso 5 Hacer
		
		Lista[i/5]= i 
		Escribir Lista[i/5]
		//comentar error, haber puesto el leer lista [1/5] // = i
	FinPara
	para i=1 Hasta 10 con paso 1 Hacer
		Lista[i] = lista[i] / 5
		//comentar error, colocar el lista [i] como un = a lista [i]
		Escribir lista(i)
	FinPara

FinAlgoritmo
