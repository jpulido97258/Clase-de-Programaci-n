Algoritmo Ejercicio_4
	Definir total Como Real
	Escribir "Ingrese el monto total de la compra"
	Leer total
	definir res1 Como Real
	Si total > 5000000 Entonces
		Res1= (55*total)/100
	SiNo
		res1= (70*total)/100
	Fin Si
	definir res2 Como Real
	Si total > 5000000 Entonces
		res2= (30*total)/100
	SiNo
		res2= 0
	Fin Si
	definir res3 como real
	si total > 5000000 Entonces
		res3=(15*total)/100
	sino 
		res3=(30*total)/100
	FinSi
	definir res4 Como Real
	res4=(res3*20)/100
	definir res5 Como Real
	res5=res4+res3
	escribir "La empresa debe invertir ", res1, " de su dinero, debe pedir ", res2, " de dinero al banco y el fabricante le dara un credito total de ", res5," donde los intereses eran de ", res4
FinAlgoritmo
