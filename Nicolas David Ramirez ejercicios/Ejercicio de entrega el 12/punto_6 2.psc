
	Algoritmo Punto_6
		Definir a,b,c,d como caracter
		Definir rta1 como entero
		Definir comple como entero
		Definir comple2 como entero
		
		Escribir "a" 
		Leer a
		Escribir "b"
		Leer b
		Escribir "c" 
		Leer c
		Escribir "d"
		Leer d
		Escribir a
		
		comple<- ConvertirANumero(a+b)
		comple2<- ConvertirANumero(c+d)
		
		si comple2 >= 50 entonces
			Escribir "Se redondea hacia arriba" 
			comple<- (comple +1) * 100 
			Escribir "el resultado es ", comple;
		SiNo
			Escribir "Se redondea hacia abajo" 
			comple<- comple * 100
			Escribir "el resultado es ", comple;
			
		FinSi
		
		
		
	
			
		
FinAlgoritmo
