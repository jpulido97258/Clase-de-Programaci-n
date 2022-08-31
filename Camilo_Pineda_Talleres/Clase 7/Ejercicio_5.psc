Algoritmo Ejercicio_5
	Definir age Como Entero;
	Definir esMayor Como Logico;
	Definir num Como Entero;
	Definir  random Como Entero;
	Definir animal Como Caracter;
	Definir favanimal Como Caracter;
	favanimal <- "zorro"
	random <- azar(50);
	Escribir "Este programa es para probar el Si, Entonces, Sino";
	Escribir "¿cuantos años tienes?";
	Leer age;
	Si age < 18 Entonces
		Escribir "Eres menor de edad, no puedes votar";
		esMayor <- Falso;
	SiNo
		Escribir "Eres mayor de edad, ya puedes votar";
		esMayor <- Verdadero;
	Fin Si;
	
	Si esMayor Entonces
		Escribir "Vamos a votar por el mejor numero, escribe cual es el mejor numero";
		Leer num;
		Escribir "Así que crees que el mejor numero es: " , num , ". Este numero tuvo " , random , " votos" 
	SiNo 
		Escribir "Como no puedes votar, escribe tu animal favorito"
		Leer animal
		animal <- Minusculas(animal)
		
		Si animal == "zorro"
			Escribir "Tu animal favorito es: " , animal , " ,A mi tambien me gusta";
		SiNo
			Escribir "Tu animal favorito es: " , animal , " ,No es mi animal favorito, pero tambien me gusta";
		FinSi;
	FinSi;
	
FinAlgoritmo
