Algoritmo Fabricante
	//definir variables
	Definir montocompra Como Real
	Definir capitalempresa Como Real
	Definir prestamobancario Como Real
	Definir creditofabricante Como Real
	Definir intereres Como Real
	Definir Montofinal Como Real
	Escribir "Escriba el monto de la factura"
	Leer montocompra
	//operaciones dependiendo el monto
	si montocompra>5000000 Entonces
		capitalempresa<- montocompra*55/100
		prestamobancario<- montocompra*30/100
		creditofabricante<- montocompra*15/100
		intereses<- creditofabricante*20/100
		
		montofinal<- capitalempresa + prestamobancario + creditofabricante + intereses
	SiNo
		si montocompra<=5000000 Entonces
			capitalempresa<- montocompra*70/100
			creditofabricante<- montocompra*30/100
			intereses<- creditofabricante*20/100
			
			montofinal<- capitalempresa + creditofabricante + intereses
		FinSi
	FinSi
	
	Escribir ("la inversion de la empresa esta representada por: "), capitalempresa;
	Escribir ("el prestamo bancario es igual a: "), prestamobancario;
	Escribir ("el credito dado por el fabricante es de: "), creditofabricante;
	Escribir ("los intereses son iguales a: "), intereses;
	Escribir ("por ultimo se podria decir que el monto final a pagar es de: "), montofinal;
	
FinAlgoritmo
