Algoritmo punto5_taller_a //63, 45, 68, 96,110,203,10,8
	dimension lista(8)
	lista(1)<-63
	lista(2)<-45
	lista(3)<-68
	lista(4)<-96
	lista(5)<-110
	lista(6)<-203
	lista(7)<-10
	lista(8)<-8
	acum<-0
	definir pro como real
	para l=1 hasta 8 Hacer
	acum<-acum+lista(l)
	FinPara
	pro<-acum/8
	escribir 'el promedio es: ',pro
FinAlgoritmo
