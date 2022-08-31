Algoritmo Punto3
	Definir A Como Entero
	Definir B Como Entero
	Definir C Como Entero
	Definir D Como Entero
	leer D
	Si D = 0 Entonces
		Escribir "La ecuacion a usar es: (A-C)^2";
		rta<- (A-C)^2
		Escribir "la respuesta es:" , rta;
	SiNo
		Si D > 0 Entonces
			Escribir "La ecuacion a usar es: (A-C)^2";
			rta2<- (A-B)^3
			Escribir "la respuesta es:" , rta2;
		SiNo
			Escribir "El numero asignado no es correcto";
		Fin Si
		
	Fin Si
FinAlgoritmo
