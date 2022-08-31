Algoritmo expresion
	// Aqui defino las variables que voy a utilizar.
	Definir p,q,resultado Como Entero;
	
	//Aqui pido el valor de las variables.
	Escribir "Por favor, ingrese el valor entero de P Y Q";
	Leer p,q;
	
	// Aqui hago los calculos:
	
	resultado <- (p^3) + (q^4) - (2*(p^2))
	
	// Aqui se hace la comprobacion:
	
	Si resultado > 680 Entonces
		Escribir "El resultado de la operacion es: " , resultado
		Escribir "P y Q satisfacen la expresión";
	SiNo
		Escribir "El resultado de la operacion es: " , resultado
		Escribir "P y Q no Satisfacen la expresión";
	FinSi
	
FinAlgoritmo
