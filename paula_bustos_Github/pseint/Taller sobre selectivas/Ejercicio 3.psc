//Dados los datos A, B, C y D que representan números enteros; escriba un 
//algoritmo que calcule el resultado de las siguientes expresiones:
// Si D=0 			(A-C)^2
// Si D=0 			((A-B)^3)/D
Algoritmo Taller_selectivas3
	Escribir "Por favor ingrese los datos"
	
	Escribir "Escriba el valor de a"
	Definir a Como Entero
	Escribir "Escriba el valor de b"
	definir b Como Entero
	Escribir "Escriba el valor de c"
	Definir c Como Entero
	Escribir "Escriba el valor de d"
	definir d Como Entero
	
	Leer a,b,c,d
	
	Si D = 0 Entonces
		ecuacion = (a-c)^2
		Escribir "El resultado es: ", ecuacion;
	SiNo
		Si D > 0 entonces
			ecuacion2 = ((a-b)^3)/d
			Escribir "El resultado es: ", ecuacion2;
		Finsi
	FinSi
FinAlgoritmo