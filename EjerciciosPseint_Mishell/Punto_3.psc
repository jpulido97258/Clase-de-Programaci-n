Algoritmo Punto_3
	definir a,b,c,d,d1,d2 como enteros;
	escribir "escriba un valor";
	leer a;
	escribir "escriba un valor";
	leer b;
	escribir "escriba un valor";
	leer c;
	escribir "escriba un valor";
	leer d;
	
	d1<-((a-c)^2);
	d2<-((a-b)^3);
	
	si d>0 entonces 
		escribir "total de expresión: " ,d1;
		sino 
			escribir"total de expresión: " ,d2;
	FinSi
FinAlgoritmo
