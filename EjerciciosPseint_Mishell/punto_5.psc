Algoritmo punto_5
	definir ventas,sueldo,p1, v1 Como real;
	escribir "Escriba el total de las ventas";
	leer ventas;
	escribir "Escriba su sueldo";
	leer sueldo;
	
	si ventas >.33 entonces
		escribir "Total de su sueldo con el extra",(sueldo +ventas )*.20;
	SiNo
		escribir"Total de su sueldo sin el extra", sueldo;
	FinSi
	
FinAlgoritmo
