Algoritmo Punto_2
	Definir num1 Como Real
	Definir sueldo Como Real
	Definir sueldo2 Como Real
	Escribir 'Salario Bruto del trabajador'
	Leer num1
	Si num1 < 900000 Entonces
		Escribir 'El sueldo tendrá un aumento del 15%'
		sueldo <- num1 * 0.15
		Escribir 'El sueldo total es:', sueldo
	SiNo
		Escribir 'El sueldo tendrá un aumento del 12%'
		sueldo2 <- num1 * 0.12
		Escribir 'El sueldo total es:', sueldo2
	Fin Si
	
FinAlgoritmo
