Algoritmo ejercicio_5
	Definir Dep1,Dep2, Dep3, RtaT1, Rta1, Rta2, Rta3,Rta4,RtaT2 Como Real
	Escribir "Digite las ventas del primer departamento"
	Leer Dep1
	Escribir "Digite las ventas del segundo departamento"
	Leer Dep2
	Escribir "Digite las ventas del tercer departamento"
	Leer Dep3
	Rta1<-Dep1+Dep2+Dep3
	Escribir "El importe total de las ventas es:", Rta1;
	Si Dep1>=Rta1*0.33 Entonces
		Rta2<-Dep1*0.20
		Escribir "El departamento 1 genero un 33% o mas de ventas en el importe total"
		Escribir "Eso lo hace ganar un 20% extra: ",Rta2;
		
	SiNo
		Si Dep2>=Rta1*0.33 Entonces
			Rta3<-Dep2*0.20
			Escribir "El departamento 2 genero un 33% o mas de ventas en el importe total"
			Escribir "Eso lo hace ganar un 20% extra: ",Rta3;
		SiNo
			Si Dep3>=Rta1*0.33 Entonces
				Rta4<-Dep3*0.20
				Escribir "El departamento 3 genero un 33% o mas de ventas en el importe total"
				Escribir "Eso lo hace ganar un 20% extra: ",Rta4;
			SiNo
				Si Dep1=Rta1*0.33 Entonces
					Escribir "Todos los departamentos generaron un 33$ de ventas en el importe total"
					
				FinSi
			FinSi
		FinSi
	FinSi
	Escribir "Al Final del mes los vendedores recibiran"
	Escribir "Vendedor 1:  ",Rta2+Dep1
	Escribir "Vendedor 2:  ",Rta3+Dep2
	Escribir "Vendedor 3:  ",Rta4+Dep3
	
FinAlgoritmo
