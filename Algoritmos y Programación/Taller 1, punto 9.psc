Algoritmo Punto_9
	Escribir "Escriba el precio de la compra"
	
	
	Definir a Como real
	definir b Como real
	Definir c Como real
	Definir d Como Real
	Definir e Como Real
	leer a
	b=0.05
	c=0.11
	d=0.18
	e=0.25
	
	si a<= 50000 Entonces
		Escribir "Su compra no posee descuento"
	FinSi
	
	Si a >50000 y a<=100000 Entonces
		b <- a*b
		b <- a-b 
		Escribir "Debe pagar: " b;
			
	FinSi
	
	si a>100000 y a<=700000 Entonces
		c <- a*c
		c <- a-c
		Escribir "debe pagar: " c;
	Fin Si
	
	si a>700000 y a<=1500000 Entonces
		d <- a*d
		d <- a-d
		Escribir "debe pagar: " d;
	Fin Si
	
	si a>1500000 Entonces
		e<- a*e
		e<- a-e
		Escribir "debe pagar: " e;
	FinSi
FinAlgoritmo