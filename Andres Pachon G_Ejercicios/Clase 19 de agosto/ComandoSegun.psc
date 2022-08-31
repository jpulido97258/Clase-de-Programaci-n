Algoritmo ComandoSegun
	Definir nota Como Entero
	Leer nota
	
	Segun nota Hacer
			100:
				Escribir "Aprobaste con exito"
			80:
				Escribir "Aprobaste";
			50:
				Escribir "Has reprobado, has de intentar de nuevo";
			10:
				Escribir "Has desaprobado con ganas";
				
			De Otro Modo:
				si nota<100 & nota>80 Entonces
					Escribir "Enhorabuena has aprobado"
				SiNo
					si nota<80 & nota>=60 Entonces
						Escribir "aprobaste por los pelos!"
					SiNo
						si nota<60 & nota>30
							Escribir "reprobaste"
						SiNo
							si nota<30 & nota>10 Entonces
								Escribir "echale un poco mas de ganas"
							SiNo
								si nota<10 Entonces
									Escribir "Eres un fracaso"
								FinSi
							FinSi
						FinSi
					FinSi
				FinSi
			
			
	FinSegun
	
FinAlgoritmo
