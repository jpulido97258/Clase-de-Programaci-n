Algoritmo Ultimo_ex
	//definiciones
	Definir monto Como Real
	Definir descuento Como Real
	Escribir ("Vas a una tienda y compras algo, escribe el monto de la compra")
	Leer monto
	
	si monto<50000 Entonces
		descuento<-0
		Escribir ("El descuento de la compra es igual a: "), descuento;
		Escribir ("El valor de su factura se mantiene en: "), monto;
	SiNo
		si	monto>= 50000 & monto<= 100000 Entonces
			descuento<- monto*5/100
			Escribir ("El descuento de la compra es igual a: "), descuento;
			Escribir ("el nuevo valor de su factura es de: "), monto-descuento;
		SiNo
			si monto>= 100000 & monto<= 700000 Entonces
				descuento<- monto*11/100
				Escribir ("El descuento de la compra es igual a: "), descuento;
				Escribir ("el nuevo valor de su factura es de: "), monto-descuento;
			SiNo
				si monto>= 700000 & monto<= 1500000 Entonces
					descuento<- monto*18/100
					Escribir ("El descuento de la compra es igual a: "), descuento;
					Escribir ("el nuevo valor de su factura es de: "), monto-descuento;
				SiNo
					si monto> 1500000 Entonces
						descuento<- monto*25/100
						Escribir ("El descuento de la compra es igual a: "), descuento;
						Escribir ("el nuevo valor de su factura es de: "), monto-descuento;
					FinSi
			FinSi
		FinSi
	FinSi
FinSi

FinAlgoritmo
