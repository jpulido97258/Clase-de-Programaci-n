Algoritmo Trabajo_mio
	Escribir "Vamos a calcular una quincena"
	Definir num como entero
	Definir sueldo como entero 

	Definir sueldo2 como entero
	
	
	Definir notrabajo como entero 
	
	Definir mastrabajo como entero 
	
	Definir mastrabajo1 como entero 
	

	
	Escribir "Colocar la cantidad de dias que trabajo"
	Leer num
	Escribir "Colocar el sueldo establecido por su trabajo"
	leer sueldo 
	Escribir "Colocar cuantos dias de mas fue"
	Leer mastrabajo
	
	

	
	notrabajo<- 15 - num
	
	variable1= notrabajo * 5
	Sueldo2 <- sueldo - variable1
	mastrabajo<- num + 15
	Si num >= 15 Entonces
		Escribir "Ganas la quincena completa"
		
	SiNo
		Escribir "Se le descuenta la cantidad de dias que no fue " , notrabajo; 
		Escribir "El valor del salario es de ", sueldo2;
		si num  > 15 Entonces
			Escribir "Se te va a aumentar el sueldo por dia"
			
		sino 
			
			
			
		FinSi
	Fin Si
	Segun num  Hacer
		15: 
			Escribir"Ganas la quincena completa "
		8:
			Escribir "Se te van a descontar 7 dias de trabajo"
		5:
			Escribir "No vas a ganar mucho dinero"
		De Otro Modo:
			
	Fin Segun
	Escribir "Colocar cuantos dias de mas fue"
	mastrabajo<- num + 15
	
	
	
FinAlgoritmo
