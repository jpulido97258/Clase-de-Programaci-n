Algoritmo Ejercicio_Taller_4 
	Definir MontoT Como Entero
	Definir Costo,total,inversiones,credito,interes,banco Como real//definicion de variables  
	Escribir "Inserte el numero de piezas"
	Leer MontoT
	Escribir "Inserte el costo de la pieza"
	Leer Costo 
	total=MontoT*costo  
	Si MontoT<5000000 Entonces
		inversion = total* .55 
		banco= total *.30
		credito=total* .15
	SiNo
		inversion= total * .70 
		banco = 0 
		credito= total * .30
	Fin Si
	Interes= credito* .20 
	Escribir "La inversion total es de: $" , inversion 
	Escribir "El dinero prestado del banco es: $" , banco 
	Escribir "El credito que se debe es de: $" ,  credito
	Escribir "El interes por el credito prestado es de: $" , Interes
FinAlgoritmo
