Algoritmo punto_4_taller
	definir costo, foem, cred, int, pres como real
	Escribir ' inserte el valor del monto total de la compra';
	leer costo;
	Si costo>5000000 Entonces;
		foem<-costo*0.55;
		cred<-costo*0.15;
		int<-cred*0.20;
		pres<-costo*0.30;
	SiNo;
		foem<-costo*0.70;
		cred<-costo*0.30;
		int<-cred*0.20;
		pres<-0;
	Fin Si;
	Escribir ' la empresa invertirá: ',foem ' cop. Pedirá prestado al banco: ',pres ' cop. Solicitará al fabricante un credito de: ',cred ' cop. Y pagará en intereses: ',int ' cop.';
FinAlgoritmo
