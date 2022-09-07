//Una  compañía  de  alquiler  de  automóviles  sin  conductor,  desea  calcular  y 
//mostrar lo que debe pagar cada cliente, de acuerdo a las siguientes 
//condiciones:
//A) Si no se rebasan los 300 km, se cancelan 50,000 COP
//B) Si la distancia recorrida es superior a 300 km
// 1) Pero inferior a 1,000 km se cobran 70,000 COP mas 30,000 COP
// por cada kilometro superior a 300 km
// 2) Si es superior a 1,000 km se cobran 150,000 COP mas 9,000 COP
// por cada kilometro adicional
Algoritmo Ejercicio_7
	Escribir "Escribir kilometros"
	Definir kilometros Como Entero
	leer kilometros
	Si kilometros < 300 Entonces
		Escribir  "El valor final es de 50,000"
	Sino
		si kilometros >= 300 y kilometros <= 1000 Entonces
			precio = 70000
			Extra = (kilometros - 300)*30000
			precio_final = precio + Extra
			Escribir "El precio a pagar es de: ", precio_final;
		SiNo
			Si kilometros >= 300 y kilometros >= 1000 Entonces
				precio = 150000
				Extra = (kilometros - 300)*9000
				precio_final = precio + Extra
				Escribir "El precio a pagar es de: ", precio_final;
			FinSi
		Finsi
	Finsi
FinAlgoritmo