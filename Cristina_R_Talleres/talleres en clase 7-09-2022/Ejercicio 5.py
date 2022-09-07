import math #nos agrega la libreria de operaciones matematicas
a=float(input ('inserta a continuación el valor del cateto opuesto ')) #define las variables y pide valores
b=float(input ('inserta a continuación el valor del cateto adyacente '))
pit=math.sqrt((a**2)+(b**2)) #realiza la operacion de que la hipotenusa es igual a la raiz cuadrada de a^2+b^2
print('cuando el cateto opuesto es igual a ',a, ' y el cateto adyacente es igual a ',b, 'la hipotenusa es igual a ',pit) #nos muestra los valores encontrados