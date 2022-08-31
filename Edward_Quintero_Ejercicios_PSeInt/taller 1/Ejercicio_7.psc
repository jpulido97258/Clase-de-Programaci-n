Algoritmo Ejercicio_7
	Definir km Como real
	//definir total Como Real
	definir total1 Como Real
	Escribir "Cuantos Kilometros recorrio?"
	leer km
	Si km <= 300 Entonces
		total1=50000
	SiNo
		Si km > 300 Entonces
			Si km <= 1000 Entonces
				total1=((km-300)*30000)+70000
			SiNo
				
			Fin Si
		SiNo
			
		Fin Si
	Fin Si
	Si km > 1000 Entonces
		total1=total+((km-1000)*9000)+150000
	SiNo
		
	Fin Si
	Escribir "Su cobro sera por " total1, " COP"
FinAlgoritmo
