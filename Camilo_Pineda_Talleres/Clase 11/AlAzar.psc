Algoritmo sin_titulo
	Definir aceptar Como Logico;
	Definir input Como Caracter;
	Definir nota Como Real;
	aceptar <- Falso
	
	Escribir "¿Crees que tienes suerte?"
	Escribir "escribe si para sacar aleatoriamente tu nota de algoritmos y programacion"
	Leer input;
	input <- Minusculas(input);
	Si input == "si" Entonces
		aceptar <- Verdadero;
	SiNo
		Escribir "Que aburrido, seguro sacabas un 100 y lo perdiste"
	FinSi
	
	Si aceptar == Verdadero Entonces
		nota <- azar(100);
		Escribir "Tu nota es: " , nota;
		Si nota >= 60 Entonces
			Escribir "Parece que tuviste suerte";
		SiNo
			Escribir "Mejor me quedaba con la nota del profesor...";
		FinSi
	FinSi
	
FinAlgoritmo
