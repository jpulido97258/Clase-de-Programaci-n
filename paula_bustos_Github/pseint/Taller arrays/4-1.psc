//Desarrolle un Array que contenga todos los n�meros del 1 al 100,
//posteriormente imprima por pantalla solo los m�ltiplos de 3 que est�n en el arreglo.
Algoritmo punto_4
	Dimension lista[100]
	//Esta parte es la lista hasta 100
	para i = 1 hasta 100 Hacer
		lista[i] = i
	FinPara
	//Esta parte hace que salten esos 100 numeros y deje solo los multiplos
	para k = 3 hasta 100 Con Paso 3
		Escribir Sin Saltar ",", lista[k]
	FinPara
FinAlgoritmo