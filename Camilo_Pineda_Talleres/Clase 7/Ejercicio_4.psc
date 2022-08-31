Algoritmo Ejercicio_4
	
	Escribir "Inicio nuevo codigo";
	Definir num Como Entero;
	Definir res Como Entero;
	Definir divres Como Entero;
	Definir resta Como Entero;
	Definir restares Como Entero;
	Definir multiplicar Como Entero;
	Definir multires Como Entero;
	
	// Suma
	Escribir "Vamos a sumar un 1 al numero que ingreses, ingresa un numero"
	Leer num; 
	res <- num + 1; // Aqui definimos que el resultado sea igual al numero ingresado por el usuario +1
	Escribir "La suma correcta es: " , res; // mostramos el resultado 
	
	// Division
	Escribir "Ahora vamos a dividir ese resultado entre 3";
	// error en esta parte -> divres esta definido como un entero, por lo que no puede tener valores decimales, esto complica la division.
	divres <- trunc(res / 3); // Aqui dividimos el resultado entre 3 y con trunc() dejamos solo la parte entera.
	Escribir "la division correcta (sin decimales) es: " , divres;
	
	// Resta
	Escribir "Ahora le restaremos un numero, escribe un numero";
	Leer resta;
	restares <- divres - resta; // aqui tomamos el resultado de la division y le restamos el valor que quiera el usuario.
	Escribir "La resta correcta es: " , restares;
	
	// multiplicar
	Escribir "Ahora lo multiplicaremos, escribe un numero";
	Leer multiplicar;
	multires <- multiplicar * restares; // aqui tomamos el resultado de la resta y lo multiplicamos por el numero que desee el usuario.
	Escribir "La multiplicación correcta es: " , multires;
	
	
	
	
	
	
	
	
	
FinAlgoritmo
