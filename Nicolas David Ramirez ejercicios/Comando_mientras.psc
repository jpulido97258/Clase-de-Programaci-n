Algoritmo Comando_mientras
	definir ulogin Como Caracter
	definir pass Como Caracter
	Definir contador como entero
	leer ulogin
	leer pass
	contador = 1
	
	Mientras contador <= 3 Hacer
		Escribir "Inserte su usuario"
		leer unlogin
		Si unlogin == "Admin" entonces
			Escribir "Usuario correcto"
			contador = 4
			
			
		
		FinSi
		
		si contador == 3 Entonces
			Escribir "Lo siento ha fallado 3 veces"
		FinSi
		Mientras contador <= 3 Hacer
			Escribir "Inserte contraseña"
			Leer pass
			si pass == "algoritmos" Entonces
				
			Escribir "Contraseña correcta"
			FinSi
		FinMientras
		
		
		Escribir ""
	Fin Mientras
	
FinAlgoritmo
