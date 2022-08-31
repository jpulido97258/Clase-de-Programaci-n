Algoritmo ejercicio_5
	definir reporte1 como real
	definir reporte2 Como Real
	definir reporte3 Como Real
	Escribir "cual fue el reporte de los departamento de ventas?"
	Escribir "Departamento A"
	Leer reporte1
	Escribir "Departamento B"
	Leer reporte2
	Escribir "Departamento C"
	Leer reporte3
	Escribir "cual fue el reporte de las ventas totales?"
	definir reportetotal Como Real
	leer reportetotal
	Escribir "cual es el salario bruto?"
	Definir salario como real
	Leer salario
	definir res1 Como Real
	res1=reportetotal-((77*reportetotal)/100)	
	definir aunsalario1 Como Real
	Si reporte1 >= res1 Entonces
		Aunsalario1=salario+((20*salario)/100)
	SiNo
		aunsalario1=salario
	Fin Si
	definir res2 como real
	res2=reportetotal-((77*reportetotal)/100)
	definir aunsalario2 Como Real
	Si reporte2 >= res2 Entonces
		Aunsalario2=salario+((20*salario)/100)
	SiNo
		aunsalario2=salario
	finsi
	definir res3 como real
	res3=reportetotal-((77*reportetotal)/100)
	definir aunsalario3 Como Real
	Si reporte3 >= res3 Entonces
		Aunsalario3=salario+((20*salario)/100)
	SiNo
		aunsalario3=salario
	finsi
	escribir "El departamento A tendra un salario de ", aunsalario1
	escribir "El departamento B tendra un salario de ", aunsalario2
	escribir "El departamento C tendra un salario de ", aunsalario3
FinAlgoritmo
