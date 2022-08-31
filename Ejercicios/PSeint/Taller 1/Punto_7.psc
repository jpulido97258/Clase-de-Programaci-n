Algoritmo Punto_7
	Definir km Como Entero
	Escribir '¿Cuanto reabasa el carro?'
	Leer km
	Si km > 300 Entonces
		Si km < 1000 Entonces
			Escribir 'Se cobraran 70000 mas 30000 por cada kilometro superior a los 300'
		SiNo
			Escribir 'Se cobraran 150000 mas 9000 por cada kilometro adicional'
		Fin Si
	SiNo
		Escribir 'Se cancelan 50000'
	Fin Si
FinAlgoritmo
