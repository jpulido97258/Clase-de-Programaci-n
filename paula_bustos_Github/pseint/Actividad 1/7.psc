//Almacene en un arreglo 10 datos digitados por consola,
//ya sean valores enteros o cadenas de texto, luego el código deberá separar los valores enteros
//de las cadenas de texto en otros arreglos y posteriormente imprimirlos por pantalla.
Algoritmo punto_7
	Dimension datos[10]
	Dimension num[10]
	Dimension string[10]
	definir a Como Entero
	definir e Como caracter
	definir i Como Entero
	Para i =0 Hasta 10 Hacer
		Leer e
		datos[i] = e
	Fin Para
	text = ConvertirANumero(datos[1])
	num = ConvertirATexto(num[1])
	
FinAlgoritmo
