Algoritmo test_preguntas
	Definir nombre Como Caracter
	Definir contador Como Entero
	Escribir "A continuacion va a realizar un test que consta de 5 preguntas, por favor digite su nombre:    "
	Leer nombre
	Escribir "Muy bien " nombre ", prepárese, la nota se dará a lo último del examen"
	Escribir "1. ¿Cuantos huesos tiene el cuerpo humano?"
	Definir respuesta1 Como Caracter
	Definir a Como Entero
	Leer respuesta1
	Segun respuesta1 Hacer
		"206":
			Escribir "¡Es correcto!"
			a<-20
		De Otro Modo:
			Escribir "Te has equivocado"	
			a<-0
	Fin Segun
	Escribir "2. ¿Cual es la capital de colombia?"
	Definir respuesta2 Como Caracter
	Definir b Como Entero
	Leer respuesta2
	Segun respuesta2 Hacer
		"Bogotá", "Bogota", "bogotá", "bogota":
			Escribir "¡Es correcto!"
			b<-20
		De Otro Modo:
			Escribir "Te has equivocado"
			b<-0
	FinSegun
	Escribir "3. ¿Cual es el primer elemento de la tabla periódica?"
	Definir respuesta3 Como Caracter
	Definir c Como Entero
	Leer respuesta3
	Segun respuesta3 Hacer
		"Hidrógeno", "Hidrogeno", "hidrógeno", "hidrogeno":
			Escribir "¡Es correcto!"
			c<-20
		De Otro Modo:
			Escribir "Te has equivocado"	
			c<-0
	FinSegun
	Escribir "4. ¿Cuál es el océano mas grande del mundo"
	Definir respuesta4 Como Caracter
	Definir d Como Entero
	Leer respuesta4
	Segun respuesta4 Hacer
		"Pacífico", "Pacifico", "pacífico", "pacifico":
			Escribir "¡Es correcto!"
			d<-20
		De otro modo:
			Escribir "Te has equivocado"
			d<-0
	FinSegun
	Escribir "5. ¿En qué año acabó la segunda guerra mundial?"
	Definir respuesta5 Como Caracter
	Definir e Como Entero
	Leer respuesta5
	Segun respuesta5 Hacer
		"1945":
			Escribir "¡Es correcto!"
			e<-20
		De Otro Modo:
			Escribir "Te has equivocado"
			e<-0
	FinSegun	
	Escribir "Su nota es:   " a + b + c + d + e
FinAlgoritmo
