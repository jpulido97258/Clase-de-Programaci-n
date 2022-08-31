Proceso punto5_arrays
	//63, 45, 68, 96,110,203,10,8 
	definir suma,promedio como real;
	definir m,x Como Entero;
	suma<-0;
	promedio<-0;
	dimension vector[8];
	
	para x <- 1 hasta 8 con paso 1 Hacer
		Escribir "ingrese el  siguiente valor: 63, 45, 68, 96,110,203,10,8 ";
		leer m;
		vector[x]<-m;
	FinPara
	
	para x<-1 hasta 8 con paso 1 Hacer
		suma<-suma + vector[x];
	FinPara
	promedio<-suma/8;
	escribir "El promedio es: ",promedio;
FinProceso
