Algoritmo ComandoFor
	Definir num Como Entero
	Leer num
	Para num <- num Hasta 10 Con Paso 1 paso Hacer
		Escribir "Es correcto hasta terminar la secuencia: " , num;
		Si num mod 2 <> 0 Entonces
			Escribir "El numero es impar"
		SiNo
			Escribir "El numero es par"
		FinSi
	Fin Para
	
FinAlgoritmo
