Algoritmo punto_5
	Definir imp Como Entero
	Definir ven Como Entero
	Definir ext Como Entero
	Definir sal Como Entero
	Definir tot Como Real
	Escribir '¿Cuanto fue la venta total?'
	Leer ven
	Escribir '¿Cuanto es el salario de cada trabajador?'
	Leer sal 
	Escribir '¿Cuanto es el importe global de las ventas?'
	Leer imp
	Escribir 'El importe global de las ventas es de:' , imp
	Si imp > (0.33 * ven) Entonces
		ext <- sal * 0.20
		tot <- ext + sal
		Escribir 'La cantidad extra que se les pagara a los trabajadores es:' , ext
		Escribir 'La cantida total que se les pagara a los trabajadores es:' , tot
	SiNo
		Escribir 'La cantidad que se les pagara a los trabajadores es' , sal
	Fin Si
FinAlgoritmo
