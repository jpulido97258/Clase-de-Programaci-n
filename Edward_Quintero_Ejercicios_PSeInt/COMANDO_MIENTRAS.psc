Algoritmo COMANDO_MIENTRAS//GENERAR UN USUARIO Y UN LOGIN EN PROGRAMA
	Definir uslogin Como Caracter
	definir pasword Como Caracter
	definir contado como entero
	leer uslogin
	leer pasword
	contador=1
	Mientras contador <= 3 Hacer
		escribir "inserte su usuario"
		leer uslogin
		si uslogin="admin" Entonces
			escribir"usuario correcto"
			contador=3
		SiNo
			escribir "usuario incorrecto"
			FinSi
		si contador>=3 entonces
			escribir "Ya fallo tres veces su usuario"
		sino
			escribir"escriba su contraseña"
		FinSi
		Escribir "Inserte su contraseña"
		leer pasword
		si pasword="algoritmos" entonces
			escribir"contraseña correcta"
		SiNo
			escribir "contraseña incorrecta"
		FinSi
		contador=contador+1
		
	FinMientras
	
FinAlgoritmo
