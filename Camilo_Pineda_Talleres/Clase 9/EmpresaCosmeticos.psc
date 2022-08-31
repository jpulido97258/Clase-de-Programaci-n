Algoritmo EmpresaCosmeticos
	// Aqui defino las variables.
	Definir sueldoEmpleados Como Entero;
	Definir ventasTotales Como Entero;
	Definir ventasDep1, ventasDep2, ventasDep3 Como Entero;
	Definir minimoVentas Como Entero;
	Definir sueldoIncentivo Como Real;
	
	Escribir "Este programa ayudara a conocer el valor de los incentivos que se daran a los empleados";
	Escribir "Primero ingrese el sueldo de los empleados"
	Leer sueldoEmpleados;
	
	Escribir "ahora ingrese el valor de las ventas de cada departamento: "
	Leer ventasDep1, ventasDep2, ventasDep3;
	
	// Calculos previos: 
	sueldoIncentivo <- sueldoEmpleados + (sueldoEmpleados * 0.2)
	ventasTotales <- ventasDep1 + ventasDep2 + ventasDep3;
	minimoVentas <- ventasTotales * 0.33;
	
	
	// Escribir en pantalla las ventas totales:
	Escribir "El valor de las ventas totales es de: " , ventasTotales
	
	// Comprobacion departamento 1:
	Si ventasDep1 > minimoVentas Entonces
		Escribir "El departamento 1 consiguio el incentivo ya que sus ventas fueron: $" , ventasDep1 , " y superaron los: $" , minimoVentas;
		Escribir "Por lo que su sueldo sera de: $" , sueldoIncentivo;
	SiNo
		Escribir "el departamento 1 no consiguio superar el minimo de ventas que era: $" , minimoVentas;
		Escribir "su sueldo seguira siendo: $" , sueldoEmpleados;
	FinSi
	
	// Comprobacion departamento 1:
	Si ventasDep2 > minimoVentas Entonces
		Escribir "El departamento 2 consiguio el incentivo ya que sus ventas fueron: $" , ventasDep2 , " y superaron los: $" , minimoVentas;
		Escribir "Por lo que su sueldo sera de: $" , sueldoIncentivo;
	SiNo
		Escribir "el departamento 2 no consiguio superar el minimo de ventas que era: $" , minimoVentas;
		Escribir "su sueldo seguira siendo: $" , sueldoEmpleados;
	FinSi
	
	// Comprobacion departamento 1:
	Si ventasDep3 > minimoVentas Entonces
		Escribir "El departamento 3 consiguio el incentivo ya que sus ventas fueron: $" , ventasDep3 , " y superaron los: $" , minimoVentas;
		Escribir "Por lo que su sueldo sera de: $" , sueldoIncentivo;
	SiNo
		Escribir "el departamento 3 no consiguio superar el minimo de ventas que era: $" , minimoVentas;
		Escribir "su sueldo seguira siendo: $" , sueldoEmpleados;
	FinSi
	
	
FinAlgoritmo
