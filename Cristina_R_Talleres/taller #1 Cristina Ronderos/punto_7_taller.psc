Algoritmo punto_7_taller
	definir km, val, sum como entero;
	escribir 'inserte a continuación la cantidad de kilometros recorridos';
	leer km;
	si km<300 Entonces;
		val<-50000;
	sino ;
		si km<1000 Entonces;
			sum<- 30000*(km-300);
			val<-70000+sum;
		SiNo;
			sum<-9000*(km-300);
			val<-150000+sum;
		FinSi;
	FinSi;
	Escribir 'segun los km recorridos (',km,') el ususario debera pagar un total de: ',val;
FinAlgoritmo
