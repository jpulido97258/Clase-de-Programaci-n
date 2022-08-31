Algoritmo punto_7
	Definir Distancia Como Entero
	Definir precio Como Entero
	Escribir "Ingresar Kilometros a recorrer"
	Leer Distancia
	Si Distancia <= 300 Entonces
		Escribir "El valor del trayecto es de: 50000 COP"
	SiNo
		Si Distancia <= 1000 Entonces
			Escribir "El valor del trayecto es de: 70000 COP; mas 30000 COP por cada km superior a 300km"
		SiNo
			Escribir "El valor del trayecto es de: 150000 COP; mas 9000 COP por cada km adicional"
		Fin Si
	Fin Si
FinAlgoritmo
