
import math #agraga la libreria de operaciones matematicas
masa=float(input(' inserta a continuación tu peso en kg '))#Define y pide unas variables al usuario
estatura=float(input(' inserta a continuación tu estatura en m '))
imc=(masa/ math.pow(estatura ,2),1)#realiza las operaciones 
print('este es tu indice de masa corporal: ',(imc)) #le da el resultado al usuario