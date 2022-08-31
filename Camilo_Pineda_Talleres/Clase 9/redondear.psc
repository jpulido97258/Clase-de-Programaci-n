Algoritmo redondear 
	// Aqui defino las variables que voy a utilizar 
	Definir a,b,c,d Como Caracter; 
	Definir comprobante Como Entero; 
	Definir num Como Entero; 
	
	// aqui solicito que le de valores a las variables a,b,c y d
	Escribir "Ingrese los valores a,b,c y d"; 
	Leer a,b,c,d; 
	
	// aqui separo los primero dos digitos y los ultimos dos digitos ya que cumpliran funciones diferentes
	comprobante <- ConvertirANumero((c + d)) 
	num <- ConvertirANumero((a + b)) 
	
	
	Si comprobante >= 50 Entonces 
		num <- (num + 1) * 100; // Si los ultimos dos numeros son mayores o iguales a 50 entonces se suma uno y se multiplica por 100 el resultado.
		Escribir "El numero redondeado es: " , num; 
	SiNo 
		num <- num * 100; // si los ultimos numeros no son mayores o iguales a 50 se multiplica por 100.
		Escribir "El numero redondeado es: " , num; 
	FinSi 
	
FinAlgoritmo 