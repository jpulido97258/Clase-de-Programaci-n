Algoritmo ejercicio_3taller120822
	Definir a,b,c,d Como Entero
	Definir Rta1,Rta2 Como Real
	Escribir "Algoritmo de Calculo"
	Escribir "Escriba A "
	Leer a
	Escribir "Escriba B "
	Leer b
	Escribir "Escriba C "
	Leer c
	Escribir "Escriba D "
	leer d
	Si d = 0 Entonces
		Escribir "D es igual a cero ya que es: ", d;
	SiNo
		Escribir "D es no es igual a cero, D es: ", d;
	FinSi
	Si d > 0 Entonces
		Escribir "D es mayor a 0, es un numero positivo, es: ", d;
	SiNo
		Escribir "D es menor a 0, es: ", d;
	FinSi
	Escribir "Se operara A - C y su resultado al cuadrado"
	Rta1<- (a-c)^2
	Escribir "El resultado es: ", Rta1;
	Escribir "Ahora se operara A - B elevado al cubo sobre D"
	Rta2<- ((a-b)^3)/d
	Escribir "El resultado es: ", Rta2;
	
	Escribir "A es igual a: ", a;
	Escribir "B es igual a: ", b;
	Escribir "C es igual a: ", c;
	Escribir "D es igual a: ", d;
	
FinAlgoritmo
