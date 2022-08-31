Algoritmo Ejercicio_2
	Escribir "Bienvenido a calcula su sueldo"
	Escribir "Por favor digite su sueldo bruto"	
	Definir sueldo Como Real
	Leer sueldo
	Definir saldo1 como real
	//Definir saldo2 como real
	//saldo1=sueldo+(sueldo+(15/100))
	//saldo2=sueldo+(sueldo+(12/100))
	Si sueldo < 900000 Entonces
		Saldo1=sueldo+(0.15*sueldo)//Escribir saldo1
	SiNo
		Saldo1=sueldo+(0.12*sueldo)
	Fin Si
	Escribir "Su salario quedara de " Saldo1
FinAlgoritmo