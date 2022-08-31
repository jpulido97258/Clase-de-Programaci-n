Algoritmo Alquiler_de_coches
	//Definir 
	Definir kilometros Como real
	Definir kilometrosx Como Real
	Definir Tarifa Como Real
	Escribir ("Escriba la cantidad de kilometros recorridos")
	
	Leer kilometros
	
	si kilometros <= 300 Entonces
		tarifa<- 50000
		Escribir ("El pago por recorrer menos de 300km es de: "), tarifa;
	SiNo
		si kilometros<=1000 Entonces
			kilometrosx<- kilometros-300
			tarifa<- kilometrosx*30000 + 70000
			Escribir ("la tarifa por recorrer menos de 1000km pero mas de 300 es de: "), tarifa;
		SiNo
			si kilometros>=1000
				kilometrosx<- kilometros-1000
				tarifa<- kilometrosx*9000 + 150000
				Escribir ("la tarifa por recorrer mas de 1000km es de: "), tarifa;
			FinSi
		FinSi
	FinSi
	
FinAlgoritmo
