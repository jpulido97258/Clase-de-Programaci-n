Algoritmo ejercicio_1taller120822 //ejercicio 1
	//Un hombre desea saber el monto de diner que obtendra por concepto de intereses
	Escribir "Monto de dinero que generara por concepto de intereses."
	Definir num1 Como Real
	Definir Rta1 Como Real
	Definir Rta2 Como Real
	Escribir "Digite la cantidad que desea invertir"
	Leer num1
	Escribir "La tasa de interes es 1.5"
	
	Rta1<-num1*1.5
	si rta1 > 100000 Entonces
		Escribir "El monto es mayor a 100.000, por lo tanto podria reinvertir."
	SiNo
		Escribir "El monto es menor a 100.000, por lo tanto no podra reinvertir."
	FinSi
	Escribir "Su monto final en su cuenta es: " , rta1; 
	
	
	
FinAlgoritmo
