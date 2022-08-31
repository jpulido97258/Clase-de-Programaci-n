Algoritmo Punto_5
	Definir depa1 como entero 
	leer depa
	Definir vendedores como entero 
	leer vendedores 
	
	vendedores <- 1500000 * 0.33 
	si vendedores = 1500000 entonces 
		Escribir "Se realiza " , vendedores + 0.20; 
	sino 
		Escribir "No se suma el 0.20 % "
	finsi
	Escribir "Se le suma"  
	si depa > 0.33 entonces 
		Escribir "Se les aumenta el 20%", depa > 0.33 + 0.20;
	sino 
		Escribir "No se aumenta nada " 
		
	FinSi
	
FinAlgoritmo
