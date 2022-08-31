Algoritmo Ejercicio_5A
	Dimension Lista[8]
	Lista[1] = 63
	Lista[2] = 45
	Lista[3] = 68
	Lista[4] = 96
	Lista[5] = 110
	Lista[6] = 203
	Lista[7] = 10
	Lista[8] = 8
	acom = 0
	Definir prom Como Real
	Para i=[1] Hasta 8 Hacer
		acom = acom + Lista[i]
	FinPara
	prom = acom/8
	Escribir 'El promedio es: ' , prom
	
FinAlgoritmo
