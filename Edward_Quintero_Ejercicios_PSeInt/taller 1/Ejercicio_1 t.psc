Algoritmo Ejercicio_1
	escribir "Hola, Bienvenido a tu calculadora de intereses"
	Escribir "¿Cual es la cuota de porcentaje de interes en tu banco? (escribe el número sin el %)"
	Definir interes Como Real
	Leer interes
	escribir "¿Cuanto dinero tienes en la cuenta de banco?"
	Definir saldo Como Real
	Leer saldo
	definir res1 Como Real
	Definir res2 como real
	res1=(interes/100)
	res2=res1*saldo
	res3=res2+saldo
	Escribir "¿Cuanto dinero quieres ganar de intereses?"
	definir val1 como real
	leer val1
	Si  res2 >= val1 Entonces
		escribir "Tus ganacias seran ", res2, " y tu cuenta tendra ",res3
	SiNo
		Escribir " el dinero en tu cuenta no genera los intereses que quieres invertir"
	Fin Si
	//Escribir "Ganaras ", res3
	//definir meses Como Real
	//leer meses
	//Definir res3 como real
	//Escribir 'El saldo en tu cuenta sera de ',res3,' en ',meses, ' meses.'; //leer res2
FinAlgoritmo