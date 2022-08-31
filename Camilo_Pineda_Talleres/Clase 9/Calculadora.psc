Algoritmo Calculadora
	// Aqui defino las variables que voy a utilizar.
	Definir a,b,c,d Como Entero;
	Definir operacion Como Entero;
	
	
	// aqui solicito al usuario saber el valor de a,b,c y d
	Escribir "Por favor ingrese el valor de los numeros A, B, C Y D";
	Leer a,b,c,d;
	
	// aqui se hacen las verificaciones y los calculos.
	Si d = 0 Entonces
		operacion <- (a - c)^2;
		Escribir "el resultado de la operacion es: " , operacion;
	FinSi
	
	Si d > 0 Entonces
		operacion <- ((a - b)^3)/ d;
		Escribir "el resultado de la operacion es: " , operacion;
	FinSi
	
	Si d <> 0 & d < 0 Entonces
		Escribir "No puedo realizar ninguna operacion, lo siento."
	FinSi
	
	
	
FinAlgoritmo
