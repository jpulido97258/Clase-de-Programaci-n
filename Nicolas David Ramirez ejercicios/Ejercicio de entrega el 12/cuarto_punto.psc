Algoritmo cuarto_punto 
	EScribir  "Una empresa quiere hacer una compra de varias piezas"
	Definir tota como entero 
	Definir dale, dale2, tota1 , tota2, tota3, tota4  como real
	leer dale
	
	si dale > 5000000 entonces 
		tota1<- dale * 0.55 
		tota2<- dale * 0.30 
		tota3<- tota1 + tota2 
		Escribir "la empresa tendrá la capacidad de invertir:" , tota3;
	sino
		Escribir "El resultado de: " , tota3;
		
	FinSi
	
	si dale  < 5000000 entonces 
		tota1<- dale * 0.70
		tota2<- dale * 0.30 
		
		Escribir "30% restante: " , tota2 ;
		
		tota4<-(tota2 * 0.20) /tota2
		
		escribir"la cantidad a invertir de los fondos de la empresa:" , dale; 
		Escribir "la cantidad a pagar a crédito: " , tota4;
		Escribir " el monto a pagar por intereses:" , tota3;
		Escribir "la cantidad prestada al banco"
	FinSi
FinAlgoritmo
