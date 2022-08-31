Algoritmo Ejercicio_3
	Escribir "Estas son las notas del curso de Algortimos y programacion";
	Definir a,b,c,d Como Entero;
	Definir promedio Como Real;
	Escribir "Ingresa las notas de los 4 estudiantes";
	Leer a,b,c,d;
	Escribir "La nota de a es: " , a;
	Escribir "La nota de b es: " , b;
	Escribir "La nota de c es: " , c;
	Escribir "La nota de d es: " , d;
	
	promedio <- (a + b + c + d) / 4 ;
	Escribir "el promedio es: ", promedio
	
	
	Si promedio > 60 Entonces
		Escribir "Aprobados"
	SiNo
		Escribir "Desaprobados" 
	FinSi
FinAlgoritmo
