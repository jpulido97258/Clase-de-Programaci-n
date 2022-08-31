Algoritmo promedio
	// aqui defino las variables que voy a utilizar.
	Definir suma Como Entero; 
	Definir resultado Como Real;
	
	Dimension num[8] //aqui defino el arreglo num y lleno cada espacio del arreglo.
	num[1] = 63;
	num[2] = 45;
	num[3] = 68;
	num[4] = 96;
	num[5] = 110;
	num[6] = 203; 
	num[7] = 10;
	num[8] = 8;
	
	Para i <- 1 Hasta 8 Hacer //aqui sumo los numeros de cada espacio del arreglo.
		suma <- suma + num[i];
	FinPara
	
	resultado <- suma / 8; //aqui divido entre 8 la suma y el resultado se coloca en la variable resultado.
	
	Escribir "El promedio es: " , resultado //aqui imprimo el resultado.
FinAlgoritmo
