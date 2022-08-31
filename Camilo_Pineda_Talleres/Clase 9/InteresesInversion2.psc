Algoritmo InteresesInversion
	// En esta parte declaro la variables que voy a estar utilizando en el programa
	Definir inversion Como Real;
	Definir intereses Como Real;
	Definir interesesPorcentaje Como Real
	Definir reinversion Como Real;
	Definir interesesObtenidos Como Real;
	Definir cuenta Como Real;
	
	
	Escribir "Este programa ayudara a calcular los intereses que se obtienen por una inversion en el banco.";
	Escribir "Y recomendara si seguir invirtiendo al superar el valor dado."
	
	// aqui solicitamos al usuario saber cuanto dinero ha invertido
	Escribir "Por favor, agregue el valor de su inversion (Sin puntos): "; 
	Leer inversion; 
	
	// aqui solicitamos al usuario saber cuantos intereses recibe cada mes.
	Escribir "Muy bien, ha invertido: $" , inversion;
	Escribir "Por favor, escriba ahora el valor porcentual de los intereses del mes, sin porcentaje.";
	Leer intereses;
	
	//aqui se realiza el calculo.
	reinversion <- 100000;
	interesesPorcentaje <- intereses / 100;
	interesesObtenidos <- inversion * interesesPorcentaje;
	cuenta <- inversion + interesesObtenidos;
	
	// aqui se comprueba si el monto supera el valor que se queria conseguir.
	Si interesesObtenidos > reinversion Entonces
		Escribir "Los intereses obtenidos son: $" , interesesObtenidos;
		Escribir "Los intereses obtenidos superan los $100.000";
		Escribir "El monto si decide invertir en la cuenta sera de: $" , cuenta;
		
	SiNo
		Escribir "Los intereses obtenidos son: $" , interesesObtenidos;
		Escribir "Los interes obtenidos NO superan los $100.000 para reinvertirlo.";
	FinSi;
	
	
	
	
	
FinAlgoritmo
