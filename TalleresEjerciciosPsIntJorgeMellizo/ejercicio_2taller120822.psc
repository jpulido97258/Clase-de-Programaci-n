Algoritmo ejercicio_2taller120822
	Definir num1,num2,Rta1,Rta2 Como Real
	Escribir 'Si su salario es menor a 900.000COP se le aplicara un 15% de aumento y un 12% en el caso que sea mayor'
	Escribir 'Digite su salario para aplicar la cantidad de aumento'
	Leer num1
	Si num1<=900000 Entonces
		Rta1 <- num1*0.15
	SiNo
		Rta1 <- num1*0.12
	FinSi
	Escribir "Su aumento seria de: " ,Rta1;
	Rta2<- Rta1+num1
	Escribir "Su salario en total seria de: " ,Rta2;
FinAlgoritmo
