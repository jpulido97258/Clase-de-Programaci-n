//Cree un arreglo del tamaño que el usuario digite por consola,
//luego el código deberá almacenar de manera aleatoria números del 0 al 1000
//en el arreglo e imprimirlos por pantalla.
Algoritmo punto_2
	Escribir "Escribe el tamaño de la lista"
	Definir a Como Entero
	leer a
	dimension lista[a]
	para i = 1 hasta a Hacer
		lista[i] = azar(1000)
		Escribir  lista[i]
	FinPara
FinAlgoritmo