Algoritmo Tercer_punto 
	Escribir "Se van a realizar las siguientes operaciones"
	Definir a,b,c,d como enteros
	Definir ope como real // mas tarde pri
	Definir ope2 como real
	Escribir "Escribir a"
	Leer a
	Escribir "Escribir b "
	Leer b
	Escribir "Escribir c "
	Leer c
	Escribir "Escribir d "
	Leer d
	//leer ope

	
	si d = 0 entonces 
		Escribir "d es igual a 0: " , d; 
	sino 
		Escribir "d no es igual a 0 "
		
	FinSi
	
	Si d < 0 entonces 
		Escribir "d es un numero negativo: " , d;
		sino 
			escribir "no aplica "
		FinSi
		
		
		Escribir  "Vamos a operar a a " 
		
		ope<- (a - c)^2
		Escribir "El resultado: " , ope; 
		
		Escribir "Vamos a operar a (a menos b) sobre d elevado al cubo"
		
		ope2<- ((a - b)^3)/d 
		Escribir "El resultado es:" , ope2;
		
		escribir "Gracias buena suerte"
		
	
		
	


	
	
FinAlgoritmo
