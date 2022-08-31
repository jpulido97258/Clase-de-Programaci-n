Algoritmo punto_2_taller
	definir sueldo, interes, aumento1, aumento2 como real;
	Escribir 'inserte a continuación el sueldo (bruto) del trabajador';
	leer sueldo;
	aumento1<- sueldo*0.15
	aumento2<- sueldo*0.12
	Si sueldo<900000 Entonces;
		interes<- sueldo+aumento1;
	SiNo;
		interes<- sueldo+aumento2;
	Fin Si;
	escribir 'el valor del sueldo despues del aumento es de: ' interes;
FinAlgoritmo
