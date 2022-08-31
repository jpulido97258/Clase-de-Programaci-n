Algoritmo punto_5
	Dimension Lista(8)
	Lista(1)= 63
	Lista(2)= 45
	Lista(3)= 68
	Lista(4)= 96
	Lista(5)= 110
	Lista(6)= 203
	Lista(7)= 10
	Lista(8)= 8
	
	Escribir "Los valores ingresados son"
	Para i = 1 Hasta 8 Hacer
		Escribir lista(i)
	FinPara
	
	Escribir "El total sumado de los valores es:"
	sum = 0
	Para i = 1 Hasta 8 Hacer
		sum = sum + lista(i)
	FinPara
	Escribir sum
	
	Escribir "El promedio de los valores es:"
	total<- sum / 8
	Escribir total
FinAlgoritmo
