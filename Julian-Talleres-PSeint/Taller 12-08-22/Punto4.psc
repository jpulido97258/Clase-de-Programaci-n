Algoritmo Punto4
	Definir num Como Entero
	Definir rta Como Entero
	Definir costo Como Real 
	Definir inversion Como Real 
	Definir banco Como Real 
	Definir cred Como Real 
	Definir interes Como Real 
	Escribir "Ingresar el numero de piezas"
	leer num
	Escribir "Ingresar el costo de la pieza"
	leer costo
	rta<- num * costo
	Escribir "El total de la compra es:" , rta;
	
	si rta > 5000000 Entonces
		inversion<- rta * 0.55
		banco<- rta * 0.30
		cred<- rta * 0.15
		Escribir "La inversion es de: $" , inversion;
		Escribir "El prestamo del banco es de: $" , banco;
		Escribir "El credito a pagar es por: $" , cred;
	SiNo
		inversion2<- rta * 0.70
		banco2<- 0
		cred<- rta * 0.30
		Escribir "La inversion es de: $" , inversion2;
		Escribir "El prestamo del banco es de: $" , banco2;
		Escribir "El credito a pagar es por: $" , cred;
	FinSi
	interes<- cred * 0.20
	Escribir "El interes por el credito es: $" , interes;
FinAlgoritmo
