//Escriba  un  algoritmo,  que  dado  como  dato  el  sueldo  de  un  trabajador,  le 
//aplique un aumento del 15% si su salario bruto es inferior a $900.000 COP y 
//12% en caso contrario. Imprima el nuevo sueldo del trabajador.
Algoritmo Taller_selectivas2
	Escribir "A continuacion se solicitara el sueldo del usuario, evitar los puntos, poner solo numeros positivos"
	Definir saldo Como Entero
	leer saldo
	Si saldo <= 900000 Entonces
		aumento = saldo * (15/100)
		saldo_con_aumento = saldo + aumento
		Escribir "El saldo del trabajador sera ahora de: ", saldo_con_aumento;
	SiNo
		aumento = saldo * (12/100)
		saldo_con_aumento = saldo + aumento
		Escribir "El saldo del trabajador sera ahora de: ", saldo_con_aumento;
	Fin Si
FinAlgoritmo