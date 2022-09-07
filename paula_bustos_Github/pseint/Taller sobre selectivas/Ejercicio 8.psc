//Dados como datos los valores enteros P y Q, determine si los mismos 
//satisfacen la siguiente expresión: P3 + Q4 ? 2*P2 > 680. En caso afirmativo debe 
//mostrar los valores  de  " P  y  Q satisfacen la expresión",  de  lo  contrario  muestre 
//un  mensaje  "P y Q no Satisfacen la expresión". Utilice la concatenación para 
//mostrar los valores
Algoritmo Ejercicio_8
	Escribir "Escribir el valor de P"
	Definir P Como Entero
	Escribir "Escribir el valor de Q"
	Definir P Como Entero
	leer P,Q
	Si P^3 + Q^4- (2*P^2) > 680 Entonces
		Escribir "P y Q satisfacen la expresion"
	Sino
		Escribir "P y Q no satisfacen la expresion"
	Finsi
FinAlgoritmo