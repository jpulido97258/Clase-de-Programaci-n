Algoritmo comando_segun //segun que nos sirve a 
	Definir nota como entero 
	leer nota
	
	Si note >= 15 Entonces
		Escribir "Es un buen momento para acercarte al profesor para hablar "
	
	SiNo
		Escribir "Esperar"
	Fin Si
	Segun nota Hacer
		100:
			Escribir "Eres pilo"
		80:
			Escribir "Aprobaste"
		50:
			Escribir "Ya casi - para la proxima"
			
		10:
			Escribir "Tienes que reflexionar"
		De Otro Modo:
			
			Escribir "Acercate a la unidad academica"
	Fin Segun
	
FinAlgoritmo
