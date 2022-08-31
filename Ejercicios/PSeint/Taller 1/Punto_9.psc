Algoritmo Punto_9
	Definir Monto,desc,tot,desc2,tot2,desc3,tot3,desc4,tot4 Como Entero
	Definir nom Como Caracter
	Escribir '¿Nombre del Comprador?'
	Leer nom
	Escribir '¿Cuanto fue el monto?'
	Leer Monto
	Si Monto < 50000 Entonces
		Escribir 'No hay desceunto'
		Escribir 'El total de la compra es: ' Monto
	SiNo
		Si Monto <= 100000 Entonces
			Escribir 'Se hara un descuento del 5%'
			desc <- Monto * 0.05
			Escribir 'El descuento es de ' desc
			tot <- Monto - desc
			Escribir 'El total a pagar es de ' tot
		SiNo
			Si Monto <= 700000 Entonces
				Escribir 'Se hara un descuento del 11%'
				desc2 <- Monto * 0.11
				Escribir 'El descuento es de ' desc2
				tot2 <- Monto - desc2
				Escribir 'El total a pagar es de ' tot2
			SiNo
				Si Monto <= 1500000 Entonces
					Escribir 'Se hara un descuento del 18%'
					desc3 <- Monto * 0.18
					Escribir 'El descuento es de ' desc3
					tot3 <- Monto - desc3
					Escribir 'El total a pagar es de ' tot3
				SiNo
					Si Monto > 1500000 Entonces
						Escribir 'Se hara un descuento del 25%'
						desc4 <- Monto * 0.18
						Escribir 'El descuento es de ' desc4
						tot4 <- Monto - desc4
						Escribir 'El total a pagar es de ' tot4
					SiNo
					Fin Si
				Fin Si
			Fin Si
		Fin Si
	Fin Si
FinAlgoritmo
