Algoritmo Ejercicio_1
	
	Definir num1 Como Entero;
	Definir num2 Como Entero;
	Definir num3 Como Entero;
	Definir res Como Entero;
	
	Escribir "Este programa... ¡Es una calculadora! (para 3 variables)";
	
	Escribir "¡Vamos a sumar! (y a restar un numero) ¡Deben ser enteros! ";
	
	// pedimos el primer numero
	Escribir "Ingresa el primer numero: "; 
	Leer num1;
	
	// pedimos el segundo numero
	Escribir  "Escribe el segundo numero que vamos a sumar: "; 
	Leer num2;
	
	// pedimos el tercer numero
	Escribir "Escribe el tercer numero que quieres restar: "; 
	Leer num3;
	
	//hacemos todo la operacion y la asignamos a la variable res -> que es el resultado
	res <- num1 + num2 - num3; 
	
	// mostramos el reultado de la operacion (y la operacion completa) 
	Escribir "El resultado de la operacion: " , num1 , " + ", num2 " - " , num3 , " = " , res; 
	
	
	
FinAlgoritmo
