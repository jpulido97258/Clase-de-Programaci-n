Algoritmo Ejercicio_Taller_1
	Definir Cant Como Real //Definicion de Cantidad de inversion 
	Definir TIntr Como Real //Definicion de Tasa de interes  
	Definir Interes Como Real// Defincion de Interes total 
	Escribir "Cantidad invertida"
	Leer Cant	
	Escribir "Ingrese su tasa de interes"
	Leer TIntr
	Interes<-Cant*TIntr
	Si Interes>100.000 Entonces
		Escribir "La cantidad generada por de interes es: $",Interes," supera los $100.000"
	SiNo
		Escribir "La cantidad generada por de interes es: $",Interes," no supera los $100.000"
	Fin Si
	Escribir "El saldo generado en la cuenta es: $",cantidad + interes
FinAlgoritmo
