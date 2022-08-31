Algoritmo redondearIdea2
	// Aqui defino las variables que voy a usar.
	Definir num Como Real;
	Definir redondeado Como Real;
	
	// Aqui se solicita el numero.
	Escribir "Ingresa el numero completo."
	Leer num;
	
	// aqui se redondea el numero, primero se divide entre 100 para tener los ultimos dos para redondear. 
	// despues se redondea y se multiplica por 100
	redondeado <- (redon(num/100)) * 100;
	
	Escribir redondeado;
	
FinAlgoritmo
