Algoritmo Punto_5
	definir Res, a, b, c, d, e, f, g, h como real
	Dimension lista(8)
	Escribir "Digite los datos"
	leer a, b, c, d, e, f, g, h
	lista(1)=a
	lista(2)=b
	lista(3)=c
	lista(4)=d
	lista(5)=e
	lista(6)=f
	lista(7)=g
	lista(8)=h
	Res=(a+b+c+d+e+f+g+h)/8
	Escribir "la lista de sus datos es"
	Para i=1 hasta 8 Hacer
		escribir lista(i)
	FinPara
	escribir "El promedio de los datos es ", Res
FinAlgoritmo
