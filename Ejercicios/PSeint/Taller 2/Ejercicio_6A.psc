Algoritmo Ejercicio_6A
	Dimension Lista[50]
	Para e=[1] Hasta 50 Hacer
		Lista[e] = e
	FinPara
	Escribir 'Los numeros que son multiplos de 5 hasta 50 son: '
	Para i=5 Hasta 50 Con Paso 5 Hacer
		Escribir Lista[i]
	FinPara
	Escribir 'Diviendo estos numeros entre 5 nos darian: '
	Para i=5 Hasta 50 Con Paso 5 Hacer
		Escribir Lista[i/5]
	FinPara
	
FinAlgoritmo
