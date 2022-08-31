Algoritmo Dados
	
	// Aqui defino la variable
	Definir tamaño Como Entero;
	// Dimension dado[tamaño] <- aqui puse la dimension y dio error ya que el tamaño no puede ser 0
	
	//Aqui pido el tamaño del arreglo
	Escribir "Ingresa el numero de dados de 1000 caras que quieres tirar";
	Leer tamaño
	
	// aqui defino la existencia del arreglo dado
	Dimension dado[tamaño]
	
	
	// Aqui con un ciclo tipo for añado por cada espacio del arreglo un numero aleatorio entre 0 y 1000 y que lo imprima en la pantalla.
	Para i <- 1 Hasta tamaño Hacer
		dado[i] = azar(1000)
		Escribir dado[i];
	Fin Para
	
FinAlgoritmo
