Algoritmo Operacion_con_tres_variables
	// asignacion de variables
	Definir num1 Como Entero;
	Definir num2 Como Entero;
	Definir num3 Como Entero;
	Definir num4 Como Entero;
	
	Escribir ("digite un numero que sea mayor a 7");
	Leer num1;
	si num1>7 Entonces
		Escribir ("El numero ingresado es valido");
	SiNo
		Escribir ("Numero invalido, inicie de nuevo")
		Repetir
			Leer num1;
		Hasta Que num1>7;
	FinSi

	Escribir ("digite un segundo numero");
	Leer num2;
	si num2>num1 Entonces
		Escribir ("El numero ingresado es mayor al primero");
	SiNo
		Escribir ("El numero ingresado es menor al primero");
	FinSi

	Escribir ("digite un tercer numero, diferente de 0");
	Leer num3;
	si num3>0 Entonces
		Escribir ("El numero ingresado es valido");
	SiNo
		Escribir ("El numero ingresado no es valido, elige otro mayor a 0");
		Repetir
			Leer num3;
		Hasta Que num3>0;
	FinSi
	
	Escribir ("digita un cuarto numero,");
	Leer num4
	si num4<num3 Entonces
		Escribir ("el numero 4 es menor que el 3")
	SiNo
		Escribir ("el 4 es mayor que el 3")
		
	FinSi
FinAlgoritmo

	