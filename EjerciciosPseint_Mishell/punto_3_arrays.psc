Algoritmo punto_3_arrays

	dimension lista(5)
	para contador <- 1 hasta 5 Con Paso 1 Hacer
		escribir"ingrese un numero entre el 1 y 5"
		leer lista[contador]
	FinPara
	Para a <- 1 hasta 5 con paso 1 hacer			
        Para ax <- a hasta 5 con paso 1 hacer			
            Si lista[a] > lista[ax] Entonces
                A <- lista[a];
                lista[a] <- lista[ax];
                lista[ax] <- A;					
            FinSi
        FinPara	
	FinPara
	Para contador = 1 hasta 5 con paso 1 hacer			
        Escribir Sin Saltar lista[contador], " ,";
    FinPara
	
	
FinAlgoritmo

		