Algoritmo Ventas_departamentos
	Definir Ventastotales Como Real
	Definir sec1 Como Real
	Definir sec2 como real
	Definir sec3 Como Real
	Escribir "ingresa un valor de las ventas totales de la empresa"
	Leer Ventastotales
	Escribir "Escribe las ventas de cada sector, las ventas de todos los sectores no deben exceder las ventas totales"
	Leer sec1
	Leer sec2
	Leer sec3
	
	si sec1< Ventastotales*0.3 Entonces
		Escribir "el sector 1 no gano ninguno beneficio"
	SiNo
		sec1<- sec1*20/100 + sec1
		Escribir "el sector 1 gano el beneficio su sueldo quedo en: " , sec1
	FinSi
	si sec2<Ventastotales*0.3 Entonces
		Escribir "el sector 2 no gano ninguno beneficio"
	SiNo
		sec2<- sec2*20/100 + sec2
		Escribir "el sector 2 gano el beneficio su sueldo quedo en: " , sec1
	FinSi
	si sec3<Ventastotales*0.3 Entonces
		Escribir "el sector 3 no gano ninguno beneficio"
	SiNo
		sec3<- sec3*20/100 + sec3
		Escribir "el sector 3 gano el beneficio su sueldo quedo en: " , sec3
	FinSi
FinAlgoritmo
