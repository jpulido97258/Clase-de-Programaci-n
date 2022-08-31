Algoritmo punto_1
	definir n,int,n1 Como Real;
	Escribir"Escriba la cantidad de dinero que usted invirtió";
	leer n1;
	escribir "Escriba el valor de la tasa de interes";
	leer n;
	
	int<- n1 * n;
	
	si int > 1000000 Entonces
		escribir "el total de intereses son:"  , int;
	SiNo
		escribir "el total de intereses son:"  , int;
		FinSi
		escribir "El total de la cuenta con intereses es de:", n1 + int;
	
FinAlgoritmo
