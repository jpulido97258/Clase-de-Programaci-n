Funcion num <- numtotal (total)
	num+total+0.5
	
Fin Funcion

Algoritmo Ejercicio_Comando_Funcion
	definir numtotal Como real
	leer numtotal
	definir num Como real
	definir total Como real
//	leer num1, num2, num3, num
	
	Si numtotal > 10  Entonces
		Escribir "El total es mayor"
	SiNo
		escribir "el total es ", numtotal;
		Si total < 10  Entonces
			escribir "el total es menor", total;
		Fin Si
	Fin Si
FinAlgoritmo
