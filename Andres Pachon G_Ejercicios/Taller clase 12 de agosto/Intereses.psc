Algoritmo Intereses
	Escribir ("Aqui se ayudara a calcular los intereses que se obtendran a partir de una inversion");
	Definir TasaDeInteres Como real;
	Definir Inversion Como Real;
	Definir Meses Como Entero;
	Definir InteresFinal Como Real;
	// aqui se ingresan los datos requeridos para aplicar la formula de interes 
	
	Escribir ("Elige la tasa de interes mensual (entre un 5 a 30%)");
	Leer TasaDeInteres
	Escribir ("Escoja la cantidad de meses, maximo 12")
	Leer Meses
	
	Escribir ("ingrese el monto que va a invertir, en pesos");
	Leer Inversion
	
	InteresFinal = Inversion * TasaDeInteres * Meses / 12
	
	Escribir ("el interes obtenido de la inversion fue: "), InteresFinal;
	
FinAlgoritmo
