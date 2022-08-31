Algoritmo Ejercicio_Taller_2
	Definir Sueldo Como Real//Definicion de salario del usuario 
	Definir Total Como Real//Defincion de salario total mayor de 900.000
	Definir Total2 Como Real//Defincion de salario total menor de 900.000
	Escribir 'Ingresa tu salario (Sin puntos)'
	Leer Sueldo
	Si Sueldo>900000 Entonces
		Total <- (Sueldo)*0.15 
		Escribir "Su sueldo total es de:",Total
		Escribir "Su seldo aumneto un 15%"
	SiNo 
		Total2 <- (Sueldo)*0.12
		Escribir "Su sueldo total es de:",Total2 
		Escribir "Su sueldo aumneto un 12%"
	FinSi
FinAlgoritmo
