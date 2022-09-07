//Una empresa que comercializa cosméticos tiene organizados a sus 
//vendedores en tres departamentos y ha establecido un programa de 
//incentivos para incrementar su productividad. El gerente, al final del mes, 
//pide el importe global de las ventas de los tres departamentos y aquellos que 
//excedan el 33% de las ventas totales se les paga una cantidad extra 
//equivalente al 20% de su salario bruto mensual.  Si todos los vendedores 
//ganan lo mismo, determinar cuánto recibirán los vendedores de los tres 
//departamentos al finalizar el mes.
Algoritmo Taller_selectivas5
	Escribir "Teniendo en cuenta que todos los tres departamentos ganaron lo mismo, ponga el valor"
	Definir vendedores Como Entero
	leer vendedores
	Escribir "Escriba el importe global de los tres departamentos"
	Definir  importe_global Como Entero
	leer importe_global
	
	opcion1 = importe_global * (33/100)
	
	Si vendedores > opcion1 Entonces
		extra = vendedores * (20/100)
		resultado = extra + vendedores
		Escribir "El valor total es: ", resultado;
	SiNo
		si vendedores < opcion1 entonces
			Escribir "Los vendedores ganaran el mismo valor de inicio que es ", vendedores;
		FinSi
	Fin Si
FinAlgoritmo