Algoritmo Proyecto_Pt3
	//definir variables
	Definir montoT Como Real
	Definir inversion Como Real
	Definir creditoF Como Real
	Definir intereses Como Real
	Definir prestacionB Como Real
	//Proceso 
	Escribir "ingrese el monto total de la compra"
	Leer montoT
	//operaciones
	si montoT>5000000 entonces 
		inversion<-montoT+(montoT*0.55)
		prestacionB<-montoT+(montoT*0.3)
		creditoF<-montoT+(montoT*0.15)
		intereses<-creditoF+(creditoF*0.2)
	sino 
		inversion<-montoT+(montoT*0.7)
		creditoF<-montoT+(montoT*0.3)
		intereses<-creditoF+(creditoF*0.2)
		
	FinSi
	//resultados
	Escribir "cantidad a invertir desde los fondos de la empresa:" , inversion;
	Escribir "cantidad a pedir prestada del banco:" , prestacionB;
	Escribir "cantidad a pagar del credito del fabricante:" , creditoF;
	Escribir "cantidad a pagar de interes por el credito del fabricante:" , intereses;
FinAlgoritmo
