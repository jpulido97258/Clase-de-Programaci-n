import math #para poder realizar la raiz 
print('Vamos a hallar la hipotenusa de un triangulo rectangulo con ayuda de la ley de Pitagoras') #Se informa al usuario de lo que va a hacer
a = float (input('¿Cuantos centimetros mide el primer cateto del triangulo? ')) #imput para que el usuario añada los valores
b = float (input('¿Cuantos centimetros mide el otro cateto del triangulo? '))
h = math.sqrt((a**2)+(b**2)) #sqrt para realizar raices

print('El primer cateto elevado al cuadrado que es ' , a**2 , ' se suma con el otro cateto elevado al cuadrado que es ' , b**2 , 'para darnos la hipotenusa del triangulo')
print('La hipotenusa del triangulo es igual a: ' ,h ,'centimetros')
