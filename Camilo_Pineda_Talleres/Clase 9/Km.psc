Algoritmo CompañiaAutomoviles
	// Aqui defino las variables
	Definir costo Como Entero;
	Definir kilometros Como Entero;
	Definir kilometrosExtra Como Entero;
	
	//Aqui solicito la cantidad de kilometros
	Escribir "Ingrese los kilometros recorridos: ";
	Leer kilometros; 
	
	
	// Aqui hago la primera comprobacion, si se pasaron de los 300 o no.
	Si kilometros <= 300 Entonces
		Escribir "No se superaron los 300 kilometros"
		costo <- 50000 
		Escribir "El costo sera de: $" , costo;
		
	SiNo Si kilometros <= 1000 Entonces
			kilometrosExtra <- kilometros - 300;
			costo <- 70000 + (kilometrosExtra * 30000);
			Escribir "Se superaron los 300 pero no se excedieron los 1000."
			Escribir "El costo sera: $" , costo;
		SiNo
			kilometrosExtra <- kilometros - 1000 
			costo <- 150000 + (kilometrosExtra * 9000);
			Escribir "Se superaron los 1000 km"
			Escribir "El costo sera $" , costo;
		FinSi
		
	FinSi
FinAlgoritmo
