import math #agrega la libreria de operaciones matematicas
r=float(input('inserte el valor del radio del cilindro ')) #define las variables y pide los valores
h=float(input('inserte el valor de la altura del cilindro '))
v=(math.pi)*(r**2)*(h) #define la operación de volumen de un cilindro
a=((2*math.pi)*r*h)+((2*math.pi)*(r**2)) #define la operacion de area de un cilindro
print('el volumen del cilindro es igual a: ',v,' y el area de su superficie es igual a: ',a) #nos da los resultados