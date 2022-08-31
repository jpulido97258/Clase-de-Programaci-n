Algoritmo punto5
	Definir Sueldo Como Entero
	Definir Dep Como Entero
	Definir Dep2 Como Entero
	definir Dep3 Como Entero
	Definir total Como real
	Definir total2 como real
	Definir total3 como real
	
	Escribir "Sueldo bruto mensual:"
	leer Sueldo
	total3<- Sueldo * 0.02
	Escribir "Ventas totales dep. 1"
	leer dep
	Escribir "Ventas totales dep. 2"
	leer dep2
	Escribir "Ventas totales dep. 3"
	leer dep3
	
	total<- dep + dep2 + dep3
	Escribir "las ventas globales fueron de:" , total;
	total2<-  total * 0.33
	Escribir "Excedente del 33% fue de:" , total2;
	
	Si dep > total2 Entonces
		total4<- Sueldo + total3
		Escribir "Trabajadores del departamento 1 superaron el excedente, Sueldo nuevo=" , total4;
	Fin Si
	Si dep2 > total2 Entonces
		total4<- Sueldo + total3
		Escribir "Trabajadores del departamento 2 superaron el excedente, Sueldo nuevo=", total4;
	Fin Si
	Si dep3 > total2 Entonces
		total4<- Sueldo + total3
		Escribir "Trabajadores del departamento 3 superaron el excedente, Sueldo nuevo=", total4;
	Fin Si

	
FinAlgoritmo