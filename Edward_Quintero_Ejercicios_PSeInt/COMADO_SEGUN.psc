Algoritmo COMADO_SEGUN
	definir nota Como Real;
	leer nota;
	si nota > 15 Entonces
		escribir "muy bien"
	SiNo
		escribir "muy mal"
	FinSi
	Segun nota Hacer
		100:
			escribir "Aprobado"
		80:
			escribir "puede mejorar"
		20:
			escribir "reprobado"
		De Otro Modo:
			Escribir "vuelve a intentarlo"
	Fin Segun
FinAlgoritmo
