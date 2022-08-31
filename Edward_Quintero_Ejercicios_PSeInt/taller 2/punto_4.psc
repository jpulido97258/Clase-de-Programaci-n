Algoritmo punto_4
	dimension lista(100)

	Para b=1 Hasta 100  Hacer
		lista(b)=b
		c=b mod 3
		si c=0 Entonces
			escribir lista(b)
		Fin Si
	Fin Para
FinAlgoritmo
