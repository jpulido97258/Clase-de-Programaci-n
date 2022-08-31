Algoritmo punto_9
	Definir monto Como Entero
	Escribir "Ingresar monto total de la compra"
	leer monto
	Si monto < 50000 Entonces
		Escribir "No hay ningun descuento"
	SiNo
		Si monto <= 100000 Entonces
			Escribir "Ganaste un descuento del 5%"
			total<- monto * 0.05
			Escribir "su descuento fue de:" , total;
			total2<- monto - total
			Escribir "Su valor a pagar actual es de:" , total2;
		SiNo
			Si monto <= 700000 Entonces
				Escribir "Ganaste un descuento del 11%"
				total<- monto * 0.11
				Escribir "su descuento fue de:" , total;
				total2<- monto - total
				Escribir "Su valor a pagar actual es de:" , total2;
			SiNo
				Si monto <= 1500000 Entonces
					Escribir "Ganaste un descuento del 18%"
					total<- monto * 0.18
					Escribir "su descuento fue de:" , total;
					total2<- monto - total
					Escribir "Su valor a pagar actual es de:" , total2;
				SiNo
					Escribir "Ganaste un descuento del 25%"
					total<- monto * 0.25
					Escribir "su descuento fue de:" , total;
					total2<- monto - total
					Escribir "Su valor a pagar actual es de:" , total2;
				Fin Si
			Fin Si
		Fin Si
	Fin Si
FinAlgoritmo
