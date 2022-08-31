Algoritmo Taller
	Definir salario Como Entero	
	Definir rta Como Entero
	Definir rta2 Como Entero
	Escribir  " Ingrese su salario aqui:"
	Leer salario
	Si salario < 900000 Entonces
		Escribir "Su aumento con un 15% es:"
		rta <- salario * 0.15
		Escribir "Salario:" , rta;
		total<- salario + rta
		Escribir "Salario total:" , total;
	SiNo
		Escribir "Su aumento con un 12% es:"
		rta2 <- salario * 0.12
		Escribir "Salario:" , rta2;
		total2<- salario + rta2
		Escribir "Salario total:" , total2;
	Fin Si
FinAlgoritmo
