Algoritmo ComandoMientras //generar usuario y login en un programa
	Definir ulogin,pass Como Caracter;
	Definir user, password Como Caracter
	Definir contador Como Entero
	Leer ulogin,pass;
	contador = 1;
	// falta terminar los si entonces de los usuarios y contraseñas
	Mientras contador <= 3 Hacer
		Escribir "inserte su usuario"; 
		si ulogin == user
	Leer ulogin;
	si ulogin == "admin" Entonces
		Escribir "usuario correcto";
		contador = 4;
	SiNo
		Escribir "usuario incorrecto";
	FinSi
	
		
	FinSi
	FinMientras
	
FinAlgoritmo
