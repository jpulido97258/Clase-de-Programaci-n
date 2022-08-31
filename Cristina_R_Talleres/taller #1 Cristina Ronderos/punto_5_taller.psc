Algoritmo punto_5_taller
	definir a,b, c,d,e como entero;
	escribir 'inserte el valor del salario mensual de los trabajadores';
	leer e;
	Escribir 'inserte el valor del importe global de las ventas de los departamentos, 1, 2 y 3';
	leer a,b,c;
	d<-a+b+c;
	si a>d*0.33 Entonces;
		A<-e+(e*0.20);
	sino ;
		A<-e;
	FinSi;
	si b>d*0.33 Entonces;
		B<-e+(e*0.20);
	sino ;
		B<-e;
	FinSi;
	si c>d*0.33 Entonces;
	C<-e+(e*0.20);
sino ;
	C<-e;
FinSi;
Escribir 'el salario de los trabajadores del departamento 1 será: ',A;
Escribir 'el salario de los trabajadores del departamento 2 será: ',B;
Escribir 'el salario de los trabajadores del departamento 3 será: ',C;
FinAlgoritmo
