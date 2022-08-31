Algoritmo punto_2
	definir sueldo,s1,s2 Como Real;
	
	escribir"Escriba su sueldo";
	leer sueldo;
	
	s1<- sueldo * 15 /100
	s2<- sueldo * 12/100
	
	si sueldo <= 900000 entonces 
		escribir "Total de sueldo incluyendo el aumento de 15% :", s1 + sueldo;
	SiNo
		escribir "Total de sueldo con aumento de 12% :", s2 + sueldo; 
	FinSi
	
FinAlgoritmo
