Algoritmo Ejercicio_segun
	definir a, b, c, d, e como real
	escribir "Cuantos Jugadores van a ir al campeonato?"
	leer b
	escribir "Cuanto es el dinero de la inscripcion?"
	leer c
	escribir "Cuanto dinero tienes";
	leer d
	e=c/b
	a=d-e
	Segun a Hacer
		0:
			Escribir "tu dinero te alcanza"
		10:
			escribir "te sobra dinero"
		-10:
			escribir "te falta dinero"
		De Otro Modo:
			escribir "Nada bien"
	Fin Segun
FinAlgoritmo