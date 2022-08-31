Algoritmo ComandoMientras // Generar un usuario y un login en un programa
	Definir saveuser Como Caracter;
	Definir savepass Como Caracter;
	Definir user,pass Como Caracter;
	Definir contador Como Entero;
	contador <- 0;
	
	Leer saveuser;
	Leer savepass;
	
	Mientras contador < 3 Hacer
		Escribir "Ingrese su usuario";
		Leer user;
		Si user == saveuser
			Escribir "Usuario correcto"
			Leer pass;
			Si pass == savepass Entonces
				Escribir "Contraseña correcta"
				Escribir "Sesion iniciada"
				contador <- 4;
			SiNo
				contador <- contador +1;
				Escribir "Contraseña incorrecta";
			FinSi
		SiNo
			Escribir "Usuario incorrecto"
			contador <- contador + 1;
		FinSi
		FinMientras
		si contador == 3 Entonces
			Escribir "Ha fallado mas de tres veces y su cuenta se ha bloqueado"
		FinSi
FinAlgoritmo
