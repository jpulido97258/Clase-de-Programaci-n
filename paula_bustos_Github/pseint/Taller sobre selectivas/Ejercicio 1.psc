//Un hombre desea saber cu�nto dinero se generar� por concepto de 
//intereses sobre la cantidad que tiene en inversi�n en el banco. El decidir� 
//reinvertir los intereses siempre y cuando �stos excedan a $100.000 COP y en ese 
//caso, desea saber cu�nto dinero tendr� finalmente en su cuenta.
Algoritmo Taller_selectivas
	Escribir "A continuacion se solicitara el sueldo del usuario, evitar los puntos, poner solo numeros positivos"
	Definir saldo Como Entero
	leer saldo
	Escribir "Ahora escribira de cuantos son los intereses"
	Definir intereses Como Entero
	leer intereses
	Si intereses >= 100000 Entonces
		resultado = intereses + saldo
		Escribir "Se�or usuario, reinvierta, su saldo gracias a la anterior inversion es de: ", resultado;
	SiNo
		Escribir "Se�or usuario, no invierta de nuevo"
	Fin Si
FinAlgoritmo