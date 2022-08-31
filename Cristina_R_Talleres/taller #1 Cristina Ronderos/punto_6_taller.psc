Algoritmo punto_6_taller
	definir A,B,C,D  como caracter;
	escribir 'inserte el valor de A, B, C y D'
	leer A, B, C, D;
    Escribir 'el número insertado es: ', A,B,C,D;
	Definir numerocompleto, redondeado como real
numerocompleto<-ConvertirANumero(A+B+C+D)
redondeado<- redon(numerocompleto/100)*100
escribir redondeado
FinAlgoritmo

