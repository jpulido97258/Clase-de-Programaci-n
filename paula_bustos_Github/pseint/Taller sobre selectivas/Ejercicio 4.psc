//Una empresa quiere hacer una compra de varias piezas de la misma clase a 
//un  fabricante  de  refacciones.  La  empresa  dependiendo  del  monto  total  de  la 
//compra,  decidirá  qué  hacer  para  pagar  al  fabricante.  Si  el  monto  total  de  la 
//compra  excede  de $5.000.000  COP la empresa tendrá la capacidad de 
//invertir  de  su  propio  dinero  un 5 5 % del monto de la compra, pedir presta al 
//banco un 30% y el resto lo pagará solicitando  un  crédito  al  fabricante.  Si  el 
//monto  total  de  la  compra  no  excede  de $5.000.000 COP la empresa tendrá 
//capacidad de invertir de su propio dinero un 70% y el restante 30% lo pagará 
//solicitando crédito al fabricante. El fabricante cobra por concepto de intereses 
//un  20%  sobre  la  cantidad  que  se  le  pague  a  crédito.      Calcule  y  muestre  la 
//cantidad a invertir de los fondos de la empresa, la cantidad a pagar a crédito, 
//el monto a pagar por intereses y si es necesario, la cantidad prestada al banco.
Algoritmo Taller_selectivas4
	Escribir "Por favor ingrese el monto total de la compra"
	Definir monto_total Como Entero
	leer monto_total
	Si monto_total >= 5000000 Entonces
		inversion = monto_total * (55/100)
		pedir_prestado = monto_total * (30/100)
		credito_fabricante = monto_total * (15/100)
		
		Escribir "La cantidad a invertir de los fondos de la empresa es de: ", inversion;
		Escribir "La cantidad prestada del banco es de ", pedir_prestado;
		Escribir "La cantidad a a pagar a credito es de: ", credito_fabricante;
	SiNo
		inversion = monto_total * (70/100)
		credito_fabricante = monto_total * (30/100)
		interes_fabricante = credito_fabricante * (20/100)
		
		Escribir "La cantidad a invertir de los fondos de la empresa es de: ", inversion;
		Escribir "La cantidad a a pagar a credito es de: ", credito_fabricante;
		Escribir "El monto a pagar por intereses es de: ", interes_fabricante;
	Fin Si
FinAlgoritmo