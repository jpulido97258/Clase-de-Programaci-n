Algoritmo Sueldos
	Definir sueldo1 Como Real
	Definir sueldo2 Como Real
	Definir sueldo1Aumentado Como Real
	Definir sueldo2Aumentado como real
	// APLICAR LOS AUMENTOS A LOS TRABAJADORES SEGUN SU SALARIO
	
	Escribir ("escribe el salario del un trabajador que gane menos de 900,000 pesos")
	Leer sueldo1
	Escribir ("Se le aplicara un aumento del 15% a su salario")
	sueldo1Aumentado<- sueldo1*15/100
	sueldo1Aumentado<- sueldo1Aumentado +  sueldo1
	Escribir ("el nuevo salario de quien gana menos de 900,000 es: "), sueldo1Aumentado;
	
	Escribir ("escribe el salario del un trabajador que gane mas de 900,000 pesos")
	Leer sueldo2
	Escribir ("Se le aplicara un aumento del 12% a su salario")
	sueldo2Aumentado<- sueldo1*12/100
	sueldo2Aumentado<- sueldo2Aumentado +  sueldo2
	Escribir ("el nuevo salario de quien gana mas de 900,000 es: "), sueldo2Aumentado;
FinAlgoritmo
