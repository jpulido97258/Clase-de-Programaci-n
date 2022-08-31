Algoritmo Algoritmo3_C8
	Escribir ("Las notas de una clase de algoritmos y programacion");
	Definir a,b,c,d,e,f,g como entero;
	Definir prom Como real;
	Escribir ("Como profesor, escribe la nota de tus 7 estudiantes")
	Leer a,b,c,d,e,f,g
	
	prom<- (a + b + c + d + e + f + g) /7;
	
	Escribir "nota de a: " , a
	Escribir "nota de b: " , b
	Escribir "nota de c: " , c
	Escribir "nota de d: " , d
	Escribir "nota de e: " , e
	Escribir "nota de f: " , f
	Escribir "nota de g: " , g
	
	si prom>6 Entonces
		Escribir ("En promedio, el curso aprobo")
	SiNo
		Escribir ("En promedio, el curso no aprobo, a repetir el año")
	FinSi
	
FinAlgoritmo
	