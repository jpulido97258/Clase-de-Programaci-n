Algoritmo punto_3_taller
	definir A, B, C, D, res Como Entero;
	escribir 'inserte 4 números enteros al azar';
	leer A, B, C, D
	Si D=0 Entonces;
		res<- (A-C)^2;
		escribir 'al usar la formula el valor sera: ' res;
	SiNo;
		res<- (A-B)^3/D;
	escribir 'al usar la formula el valor sera: ' res;
		
	Fin Si;
FinAlgoritmo
