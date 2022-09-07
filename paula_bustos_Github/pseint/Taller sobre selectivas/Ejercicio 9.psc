//en  una  tienda  efectúan  un  descuento  a  los  clientes  dependiendo  del 
//monto  de  la compra.  El descuento se efectúa con base en el siguiente 
//criterio:
//	a. Si el monto es inferior a $50.000 COP, no hay descuento.
//	b. Si está comprendido entre $50.000 COP y $100.000 COP
//inclusive, se hace un descuento del 5%
//	c. Si está comprendido entre $100.000  COP y $700.000  COP 
//inclusive,  se  hace  un  descuento del 11%
//	d. Si  está  comprendido  entre  $700.000  COP  y  $1.500.000  COP 
//inclusive, el descuento es del 18
//	e. Si el monto es mayor a $1.500.000., hay un 25% de descuento.
//Calcule y muestre el nombre del cliente, el monto de la compra, monto a pagar 
//y descuento recibido.
Algoritmo Ejercicio_9
	Escribir "Escriba el monto de la compra"
	Definir monto Como Entero
	Leer monto
	Si monto < 50000 Entonces
		Escribir "No tendra descuento"
	SiNo
		Si monto >= 50000 y monto < 100000 Entonces
			descuento = monto * (5/100)
			valor_descuento = monto + descuento
			Escribir "El valor total es de: ", valor_descuento;
		Fin Si
		Si monto >= 100000 y monto < 700000 Entonces
			descuento = monto * (11/100)
			valor_descuento = monto + descuento
			Escribir "El valor total es de: ", valor_descuento;
		Fin Si
		Si monto >= 700000 y monto < 1500000 Entonces
			descuento = monto * (18/100)
			valor_descuento = monto + descuento
			Escribir "El valor total es de: ", valor_descuento;
		Fin Si
		Si monto >= 1500000 Entonces
			descuento = monto * (25/100)
			valor_descuento = monto + descuento
			Escribir "El valor total es de: ", valor_descuento;
		Fin Si
	Fin Si
FinAlgoritmo