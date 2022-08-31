Algoritmo Punto_3
	Escribir 'Vamos a hacer una operacion'
	Definir A, B, C, D Como Entero
	Definir Resultado Como Real
	Definir Resul2 Como Real
	Escribir 'Pon 3 numeros enteros cualquiera'
	Leer A, B, C
	Escribir 'Pon un numero entero que sea menor o igual a 0'
	Leer D
	Si D <= 0 Entonces
	Si D = 0 Entonces
		Resultado <- (A-C)^3
		Escribir 'El resultado es:', Resultado
	SiNo
		Resul2 <- (A-B)^3 / D
		Escribir 'El resultado es:' , Resul2
	Fin Si
	SiNo 
		Escribir 'No se puede realizar la operacion'
	FinSi
FinAlgoritmo
