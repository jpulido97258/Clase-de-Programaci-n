#ejercicio sobre variables
import math 

print("Este ejercicio nos ayudara a sacar el area y el volumen de un dodecaedro")
print("para hallar su area es necesario sumar el área de todas sus caras.")
print("Sabiendo que todas sus caras son pentágonos, pero antes de aplicar la formula del area de un pentagono hay que hallar el apotema")

#Calcular apotema de un pentagono
print("Escribe un valor para L")
L=int(input())
print("Elegiste:" ,L ,"para L")
ap= (L)/2*math.tan(36)

print("el apotema sera igual a:", ap)

#Ahora calcular el area de un pentagono

area=(5*L*ap)/(2)
#Calcular area de el dodecaedro
print("Teniendo el area de un pentagono, ahora resta multiplicar el resultado por 12, esto daria que el area es igual a:" , area*12)

#Segundo, calcular el volumen del dodecaedro

print("para hallar el volumen, ingresa un valor para las aristas: ")
aristas=int(input())

#hallar volumen del dodecaedro
print("elegiste" , aristas , "para el valor de las aristas, ahora, viene la formula del volumen")
volumen= (0.25*(15+7*(math.pow(5,1/2))))*(aristas**3)

print("El volumen es igual a: ", volumen)

