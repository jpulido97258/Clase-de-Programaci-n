Algoritmo EmpresaCompra
	//aqui defino las variables utilizare para resol
	Definir valorCompra Como Entero;
	Definir fondosPropios Como Real;
	Definir fondosPrestamo Como Real;
	Definir CreditoFabricante Como Real;
	Definir interes Como Real;
//	Definir interesCredito Como Real; Esta variable ya no se usa al corregir el error.
	
	// aqui solicito saber el monto de la compra
	
	Escribir "Este programa ayudara a su empresa a saber cuando dinero podran invertir de sus fondos, cuanto tendran que pedir prestado y cuanto a credito";
	Escribir "Escriba el monto de la compra (sin separarlo por puntos): ";
	Leer valorCompra;
	
	Si valorCompra > 5000000 Entonces
		fondosPropios <- valorCompra * 0.55;
		fondosPrestamo <- valorCompra * 0.3; 
		CreditoFabricante <- valorCompra * 0.15;
		interes <- CreditoFabricante + (CreditoFabricante * 0.2);
//		interesCredito <- CreditoFabricante + interes; Aqui me equivoque y sume algo que no tenia que sumar
		
		Escribir "La empresa podra destinar de sus fondos: $" , fondosPropios;
		Escribir "El valor del prestamo del banco es de: $" , fondosPrestamo;
		Escribir "El valor a credito es de: $" , CreditoFabricante , " Pero, tendran que pagar con intereses por: $" , interes;
		
		
	SiNo
		fondosPropios <- valorCompra * 0.7;
		CreditoFabricante <- valorCompra * 0.3;
		interes <- CreditoFabricante + (CreditoFabricante * 0.2);
//		interesCredito <- CreditoFabricante + interes; Aqui me equivoque y sume algo que no tenia que sumar
		
		Escribir "La empresa podra destinar de sus fondos: $" , fondosPropios;
		Escribir "El valor a credito es de: $" , CreditoFabricante , " Pero, tendran que pagar con intereses: $" , interes;
		
	FinSi
	
	
FinAlgoritmo
