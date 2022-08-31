Algoritmo ejercicio_4taller120822
	Definir num1,num2, num3, Rta1, Rta2, Rta3, Rta4 Como Real
	Escribir "Defina el monto total de compra"
	Leer num1
	si num1 > 5000000 Entonces
		Rta1<-num1*0.55
		Rta2<-num1*0.30
		Rta3<-Rta1+Rta2
		Escribir "El monto excede los de 5.000.000COP, por lo que le pedira prestado el 30% al banco e invertira un 55% de su propio dinero", Rta3;
	SiNo
		Rta1<-num1*0.70
		Rta2<-num1*0.30
		
		Escribir "Obtenemos un 30% restante, Este monto se pagara solicitando un credito al fabricante: ",Rta2; 
		Rta4<-(Rta2*0.20)/Rta2
	
		Escribir "Los fondos a invertir en la empresa son: ", num1;
		Escribir "La cantidad a pagar a credito es: ", Rta4;
		Escribir "El monto a pagar a intereses: ", Rta2;
		Si num1 > 5000000 Entonces
			Escribir "La cantidad prestada al banco es",Rta1;
		SiNo
			
		FinSi
		
	FinSi
FinAlgoritmo
