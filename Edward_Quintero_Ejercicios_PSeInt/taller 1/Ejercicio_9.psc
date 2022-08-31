Algoritmo Ejercicio_9
	escribir "Bienvenido, por favor escriba su nombre"
	definir nom Como Caracter
	leer nom
	Definir total Como Real
	escribir "Cual fue el total de su compra?"
	Leer total
	definir total1 Como Real
	definir des Como Real
	Si total < 50000 Entonces
		total1 = total
	SiNo
		Si total >= 50000 Entonces
			Si total <= 100000 Entonces
				des=(total*5)/100
			SiNo 
				Si total <= 700000 Entonces
					des=(total*11)/100
				SiNo
					Si total <= 1500000 Entonces
						des=(total*18)/100
					SiNo
						Si total > 1500000 Entonces
							des=(total*25)/100
						SiNo
							
						Fin Si
					Fin Si
				Fin Si
				
			Fin Si
		SiNo
			des= 0
		Fin Si
	Fin Si
	total1=total-des
	escribir nom
	escribir "El monto de su compra es " total
	Escribir "su total a pagar es de ",total1," y el descuento aplicado fue por " des 
FinAlgoritmo
