Algoritmo ComandoRepetir //se utiliza para crear ciclos.
	Definir num Como Entero;
	Escribir "Este programa pide un numero hasta que sea mayor que 10 y sea par"
	
	Leer num;
	repetir 
		Escribir "Ingrese un numero"
		
		Escribir "El numero es: " , num;
		
		Si num mod 2 <> 0 Entonces
			Escribir "El numero es impar"
		SiNo
			Escribir "El numero es par"
		FinSi
		num <- num + 1;
		
	Hasta Que num > 10;
	
FinAlgoritmo
