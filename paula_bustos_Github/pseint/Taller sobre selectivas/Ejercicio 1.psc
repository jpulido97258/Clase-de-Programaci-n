//Un hombre desea saber cuánto dinero se generará por concepto de 
//intereses sobre la cantidad que tiene en inversión en el banco. El decidirá 
//reinvertir los intereses siempre y cuando éstos excedan a $100.000 COP y en ese 
//caso, desea saber cuánto dinero tendrá finalmente en su cuenta.
Algoritmo Taller_selectivas
	Escribir "A continuacion se solicitara el sueldo del usuario, evitar los puntos, poner solo numeros positivos"
	Definir saldo Como Entero
	leer saldo
	Escribir "Ahora escribira de cuantos son los intereses"
	Definir intereses Como Entero
	leer intereses
	Si intereses >= 100000 Entonces
		resultado = intereses + saldo
		Escribir "Señor usuario, reinvierta, su saldo gracias a la anterior inversion es de: ", resultado;
	SiNo
		Escribir "Señor usuario, no invierta de nuevo"
	Fin Si
FinAlgoritmo