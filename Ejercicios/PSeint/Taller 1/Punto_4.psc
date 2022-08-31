Algoritmo Punto_4
	Definir monto Como Entero
	Definir cap Como Real
	Definir pres Como Real
	Definir cred Como Real
	Definir cap2 Como Real
	Definir cred2 Como Real
	Definir int Como Real
	Definir int2 Como Real
	Escribir '¿Cuanto es el monto total de la compra?'
	Leer monto 
	Si monto > 5000000  Entonces
		cap <- monto * 0.55
		Escribir 'La empresa tendra la capacidad de invertir:' , cap
		pres <- monto * 0.3
		Escribir 'La empresa pedirá al banco:' , pres
		cred <- monto - (cap + pres)
		Escribir 'El resto que se pagará solicitando un credito al fabricante es:' , cred 
		int <- cred * 0.2
		Escribir 'El monto a pagar por interes es de:' , cred
	SiNo
		cap2 <- monto * 0.7
		Escribir 'La empresa tendra la capacidad de invertir:' , cap2
		cred2 <- monto * 0.3
		Escribir 'El resto que se pagará solicitando un credito al fabricante es:' , cred2 
		int2 <- cred2 + 0.2
		Escribir 'El monto a pagar por interes es de:' , int2
	Fin Si
	
FinAlgoritmo
