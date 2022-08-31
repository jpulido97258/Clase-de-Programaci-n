Algoritmo Proyecto_Pt1
	// definir variables
	Definir salarioB Como Real
	Definir operacion Como Real
	Definir salarioF Como Real
	// proceso
	Escribir "ingrese su salario bruto"
	Leer salarioB
	//operaciones
	si salarioB < 900000 Entonces
		salarioF<-salarioB+(salarioB*0.15)
	sino 
		salarioF<-salarioB+(salarioB*0.12)
	FinSi
	//resultado
	Escribir "su salario final con aumento es de: " , salarioF;
FinAlgoritmo
