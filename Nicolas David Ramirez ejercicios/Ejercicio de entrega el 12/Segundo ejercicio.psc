Algoritmo sin_titulo
	Escribir "Vamos a evidenciar el aumento de una persona a su salario con la siguiente operacion" 
	Escribir "Escribir el salario que usted tiene porfavor"
	Definir salario como real
	Definir infe como real 
	leer infe
	Escribir "Si es inferior a los novecientos mil se le multiplica el 0.15 y si es mayor por el 0.12 "
	si infe <= 900000 entonces 
		salario<-infe * 0.15
	sino 
		salario<- infe * 0.12
		
	FinSi
	Escribir "Su aumento o disminucion seria de:"
	Escribir salario
		
	
	
	
	
FinAlgoritmo
