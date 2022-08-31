Algoritmo Calculadora//Para comentar y documentar doble slash
	Definir num1 Como real// primero definir la variable
	Definir num2 como real//Dar estructuras de entrada-proceso-salida
	definir num3 como real
	escribir 'Elige un numero'
	Leer num1
	escribir 'Elige un numero'
	leer num2
	Definir res Como real
	Escribir "Escribe 1 para sumar tus numeros, escribe 2 para multiplicarlos o escribe 3 para dividirlos"
	leer num3
	Si num3=1 Entonces
		res=num1+num2
	SiNo
		Si num3=2 Entonces
			res=num1*num2
		SiNo
			Si num3=3 Entonces
				res= num1/num2
			
			Fin Si
		Fin Si
	Fin Si
	
	Escribir 'Tu resultado es ' res
FinAlgoritmo
