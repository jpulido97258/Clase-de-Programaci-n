Algoritmo Proyecto_Pt4
	Definir dept1 Como Real
	Definir dept2 Como Real
	Definir dept3 Como Real
	Definir sueldo Como Real
	Definir valorT Como Real
	Definir pt33 Como Real
	sueldo <- 950000 
	Escribir "Ingresar el valor de las ventas del departamento 1"
	Leer dept1
	Escribir "Ingresar el valor de las ventas del departamento 2"
	Leer dept2
	Escribir "Ingresar el valor de las ventas del departamento 3"
	Leer dept3
	// Proceso
	valorT <- dept1+dept2+dept3;
	pt33 <- valorT * 0.33;
	Si (dept1 > pt33) Entonces
		dept1 <- sueldo + sueldo *0.2;
	Sino
		dept1 <- sueldo;
	FinSi
	// Se hace el mismo procedimiento para los tres departamentos
	Si (dept2 > pt33) Entonces
		dept2 <- sueldo + sueldo * 0.2;
	Sino
		dept2 <- sueldo;
	FinSi
	
	Si (dept3 > pt33) Entonces
		dept3 <- sueldo + sueldo * 0.2;
	Sino
		dept3 <- sueldo;
	FinSi
	// Salidas del programa
	Escribir "El sueldo de los vendedores del departamento 1 es:", dept1;
	Escribir "El sueldo de los vendedores del departamento 2 es :" , dept2;
	Escribir "El sueldo de los vendedores del departamento 3 es :" , dept3;
	
FinAlgoritmo