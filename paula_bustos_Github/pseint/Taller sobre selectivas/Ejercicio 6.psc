//Se tienen 4 d�gitos en las variables A, B, C, D que forman un entero 
//positivo N. Se desea  redondear  N  a  la  centena  m�s  pr�xima  y  mostrar  el 
//resultado. Considere los siguientes ejemplos: Si A es 2, B es 3, C es 6 y D es 2
//entonces N es 2362 y el resultado redondeado es 2400. Si N es 2342, el 
//resultado redondeado ser� 2300 y si N es 2962, el resultado redondeado ser� 3000
Algoritmo Taller_selectivas6
	Escribir "Escribir las cuatro variables"
	Definir A,B,C,D Como Caracter
	Leer A,B,C,D 
	N = ConvertirANumero(A+B+C+D)
	redondear = (redon(N/100))*100
	Escribir redondear
FinAlgoritmo