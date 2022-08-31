Algoritmo punto_4
	definir m,cost,tot como entero;
	definir credi,int,ban,inv Como Real;
	escribir " Ingrese el número de piezas que quiere comprar";
	leer m;
	escribir " Ingrese el valor de la pieza";
	leer cost;
	
	tot<- m*cost;
	
	si tot >500000 Entonces
		inv=tot* 55/100;
		ban=tot *30 /100;
		credi= tot *15/100;
		
	SiNo
		inv=tot*70/100;
		ban=0;
		credi=tot*30/100;
	FinSi
	int<-credi * 20/100;
	escribir "Total de inversión:", inv;
	escribir "Prestamos del banco:", ban;
	escribir "Credito a pagar:",credi;
	escribir"Interés por credito:",int;
	
FinAlgoritmo
