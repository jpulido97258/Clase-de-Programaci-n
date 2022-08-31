Algoritmo punto_8
	definir P Como Entero
	Definir Q Como Entero
	Escribir "Asignar valor a P"
	Leer P
	Escribir "Asignar valor a Q"
	Leer Q
	
	total<- (P)^3 + (Q)^4 -2*(P)^2
	
	Si total > 680 Entonces
		Escribir "Los valores de P y Q satisfacen la expresion:", total;
	SiNo
		Escribir "P y Q no satisfacen la expresion:", total;
	Fin Si
FinAlgoritmo
