Algoritmo ejecicio_usuario
	
	definir unlogin Como Caracter
	definir contra como caracter
	Definir contador como entero 
	Escribir "Escriba su usuario"
	leer unlogin
	Escribir "Escriba su contraseña"
	leer contra
	Escribir "Colcar su usuario"
	
	contador =  1 
	
	Mientras contador <= 3 Hacer
		Escribir "Colocar el usuario"
		Leer ulogin 
		si ulogin == "Nico" Entonces
			Contador = 2 
			
		SiNo
			Escribir "usuario incorrecto"
			
		FinSi
	leer 	
	FinMientras
	
	
FinAlgoritmo
