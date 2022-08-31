Algoritmo descuentos
	// Aqui defino las variables que voy a utilizar
	Definir nombre Como Caracter;
	Definir monto Como Real;
	Definir descuento Como Real;
	Definir montofinal Como Real;
	//Aqui pido el valor del monto y el nombre
	Escribir "¿Cual es tu nombre?";
	Leer Nombre;
	Escribir "Ingresa el monto para calcular el descuento";
	Leer monto;
	
	Si monto < 50000 Entonces
		//aqui si el monto es menor a 50.000 no hay descuento
		Escribir "¡No hay descuento!";
		Escribir nombre , ", el costo final de tu compra es: $" , monto;
	SiNo Si monto >= 50000 & monto < 100000 Entonces
			// si el monto es igual o mayor a 50.000 y menor a 100.000 entonces se descuenta el 5%
			descuento <- monto * 0.05;
			montofinal <- monto - descuento;
			Escribir "El descuento sera de 5%, lo cual es un descuento de: $" , descuento  , " que sera restado de los: $" , monto , " originales";
			Escribir Nombre, ", el valor a pagar es: $" , montofinal;
		SiNo Si monto >= 100000 & monto < 700000 Entonces
				// si el monto es mayor o igual a 100.000 se descuenta 11%
				descuento <- monto * 0.11;
				montofinal <- monto - descuento;
				Escribir "El descuento sera de 11%, lo cual es un descuento de: $" , descuento , " que sera restado de los: $" , monto , " originales";
				Escribir Nombre, ", el valor a pagar es: $" , montofinal;
			SiNo Si monto >= 700000 & monto < 1500000 Entonces
					// si el monto esta entre 700.000 y 1.500.000 se descuenta 18%
					descuento <- monto * 0.18;
					montofinal <- monto - descuento;
					Escribir "El descuento sera de 18%, lo cual es un descuento de: $" , descuento , " que sera restado de los: $" , monto , " originales";
					Escribir Nombre, ", el valor a pagar es: $" , montofinal;
				SiNo
					// si el monto es superior a 1.500.000 el descuento es del 25%
					descuento <- monto * 0.25;
					montofinal <- monto - descuento;
					Escribir "El descuento sera de 25%, lo cual es un descuento de: $" , descuento , " Sque sera restado de los: $" , monto , " originales";
					Escribir Nombre, ", el valor a pagar es: $" , montofinal;
				FinSi
			FinSi
		FinSi
	FinSi
	
FinAlgoritmo
