Algoritmo ComandoSegun
	Definir eleccion Como Entero;
	Definir num1,num2,resultado Como Real;
	Escribir "Esta es una calculadora no programada aun.";
	Escribir "Escribe el numero de lo que quieres hacer"
	Escribir "(1) Sumar , (2) Restar , (3) Dividir , (4) Multiplicar , (5) Raiz"
	eleccion <- 0;
	Leer eleccion;
	
	
	Segun eleccion Hacer // segun que permite hacer llamado a otras variables sean secuenciales o no.
		1:
			Escribir "Vamos a sumar";
			Escribir "Escribe el primer numero: ";
			Leer num1;
			Escribir "Escribe el segundo numero";
			Leer num2;
			resultado <- num1 + num2;
			Escribir "El resultado de la operacion: " , num1 , " + ", num2 , " = ", resultado;
		2:
			Escribir "Vamos a restar";
			Escribir "Escribe el primer numero: ";
			Leer num1;
			Escribir "Escribe el segundo numero";
			Leer num2;
			resultado <- num1 - num2;
			Escribir "El resultado de la operacion: " , num1 , " - ", num2 , " = ", resultado;
		3:
			Escribir "Vamos a dividir";
			Escribir "Escribe el primer numero: ";
			Leer num1;
			Escribir "Escribe el segundo numero";
			Leer num2;
			Si num2 == 0 Entonces
				Escribir "¡Esto no se puede hacer!"
			SiNo
				resultado <- num1 / num2;
				Escribir "El resultado de la operacion: " , num1 , " / ", num2 , " = ", resultado;
			FinSi
		4:
			Escribir "Vamos a multiplicar";
			Escribir "Escribe el primer numero: ";
			Leer num1;
			Escribir "Escribe el segundo numero";
			Leer num2;
			resultado <- num1 * num2;
			Escribir "El resultado de la operacion: " , num1 , " x ", num2 , " = ", resultado;
		5: 
			Escribir "Vamos a sacar la raiz cuadrada";
			Escribir "Ingresa el numero al que se sacara la raiz: "
			Leer num1;
			Escribir "Escribe el numero de la raiz"
			Leer num2;
			Si num1 < 0 & num2 <= 0 Entonces
				Escribir "ESTO NO EXISTE!" 
				Escribir "(Al menos en esta matematica)"
			SiNo
				resultado <- num1^(1/num2);
				Escribir "el resultado de la raiz ", num2 ," de "  , num1 , " = " , resultado;
			FinSi
		De Otro Modo:
			Escribir "No se selecciono una operacion";
	FinSegun;
	
	
FinAlgoritmo
