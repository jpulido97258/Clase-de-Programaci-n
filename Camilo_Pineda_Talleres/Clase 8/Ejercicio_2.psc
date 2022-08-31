Algoritmo Ejercicio_2
	// ACCION SELECTIVA
	// los numeros 1 y 2 son enteros, solo podran tomar valores enteros.
	Definir num1 Como Entero;
	Definir num2 Como Entero;
	// los numeros 3 y 4 son reales, podran tomar valores decimales
	Definir num3 Como Real;
	Definir num4 Como Real;
	
	
	Escribir "vamos a hacer una comparación entre numeros que ingreses";
	
	// primero los dos numeros enteros
	Escribir "Los primeros numeros seran enteros, ingresa el primer numero: ";
	Leer num1;
	Escribir "Ingresa el segundo numero: ";
	Leer num2;
	
	Escribir "Comprobaremos si " , num1 , " es mayor que " , num2;
	Si num1 > num2 Entonces
		Escribir "¡Efectivamente! ", num1, " es mayor que: ", num2; // aqui se comprueba si el prime numero es mayor que el segundo
	SiNo
		Escribir  "Parece que no, la verdad es que: ",  num1 , " es menor o igual que " , num2; // si no es asi el primer numero tendra que ser igual o menor que el segundo
	FinSi;
	
	// aqui se hace la comprobacion de numeros reales"
	Escribir "Muy bien, ahora podemos comprobar numeros reales";
	Escribir "Separa los decimales con un punto";
	Escribir "Ingresa el primer numero";
	Leer num3;
	
	Escribir "Ingresa el segundo numero";
	Leer num4;
	
	Escribir "Comprobaremos si los numeros ingresados son distintos";
	
	Si num3 <> num4 Entonces
		Escribir "Asi es, " , num3 , " es diferente de" , num4; // se comprueba si los dos numeros son diferentes
	SiNo
		Escribir "Parece que no, " , num3 , " es igual a " , num4; // si no son diferentes deben ser iguales.
	FinSi;
FinAlgoritmo
