Algoritmo Punto_2
	Escribir "Escriba su salario"
	
	Definir a Como Real
	Definir b Como Real
	Definir c Como Real
	b=0.12
	c=0.15
	leer a
	
	Si a <=900000 Entonces
		a <- a*c+a
		
		Escribir "Su salarios sera: " a;
	SiNo
		a <- a*b+a
		
		Escribir "Su salario sera: " a;
	Fin Si
	
	
FinAlgoritmo
