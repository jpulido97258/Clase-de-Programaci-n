Algoritmo punto_8_taller
	definir P, Q, M Como Entero;
	escribir 'inserte los valores que desea asignar a P y Q';
	leer P,Q;
	M<-P^3+Q^4-2*P^2;
	si M>680 Entonces;
		escribir 'P y Q satisfacen la expresión';
	sino 
		escribir 'P y Q no satisfacen la expresión';
	FinSi;
	//no entendi como usar la concatenación para mostrar los valores,pero hice lo demás
FinAlgoritmo
