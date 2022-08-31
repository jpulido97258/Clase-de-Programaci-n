Algoritmo Aprox_centena
	// Definir 
	Definir a,b,c,d Como real
	Definir centenar Como real
	Definir num Como real
	//evaluar
	Leer a,b,c,d
	
	num<- (a * b * c* d)
	
	centenar<- redon(num/100) * 100
	
	Escribir ("El resultado redondeado es: "), centenar;
	
FinAlgoritmo
