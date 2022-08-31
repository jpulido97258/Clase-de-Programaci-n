Algoritmo aumentoDeSueldo
	// aqui defino las variables que voy a utilizar en el programa.
	Definir sueldo Como Entero;
	Definir sueldoFinal Como Real;
	
	// aqui solicitamos el usuario conocer el valor del sueldo
	Escribir "Este programa ayudara a calcular el aumento salarial que se aplicara";
	Escribir "Ingrese el sueldo a calcular (sin separarlo por puntos): ";
	Leer sueldo;
	
	// aqui se realiza la confirmacion de si es mayor a los $900k o no
	
	Si sueldo < 900000 Entonces
		sueldoFinal <- sueldo + (sueldo * 0.15);
		Escribir "El aumento del sueldo es del 15%, por lo tanto el valor del sueldo es: " , sueldoFinal;
		
	SiNo
		sueldoFinal <- sueldo + (sueldo * 0.12);
		Escribir "El aumento del sueldo es de 12% por lo tanto el valor del sueldo es: " , sueldoFinal;
	FinSi
	
	
	
	
	
	
FinAlgoritmo
