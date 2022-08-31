Algoritmo Clasificar
	
	Dimension datos[10] //aqui defino el arreglo basico para lo que agreguen los usuarios
	Dimension datosNum[10] // Aqui defino los arreglos para clasificar.
	Dimension datosString[10]
	Definir a Como Entero;
	
	Para i <- 1 Hasta 10 Hacer //aqui repito 10 veces el pedir el valor de la posicion del arreglo.
		Escribir "Ingresa el valor para la posicion " , i , " de la lista"; 
		Leer datos[i];
		a <- ConvertirANumero(datos[i])
		Si a == datos[i]
	FinPara
	
	Para i <- 1 Hasta 10 Hacer
		Escribir datos[i] , ", " Sin Saltar
	FinPara
	
	
FinAlgoritmo
