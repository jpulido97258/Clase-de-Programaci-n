#Proyecto de convertidor de moneda en python - Jorge Mellizo - 



print("Bienvenidos al convertidor de moneda ")
print("Que moneda quieres convertir")

A= ("Dolar, Euro, Peso Colombiano, Peso Argentino, Yuan Chino, libra esterlina")
#print(A)
print(A)
print("Seleccione la posicion, 0:5")
B=input()
moneda=str(A.index(B)) #Corregir error 
print(moneda) #error  #Traceback (most recent call last):
  #File "c:\Users\SALA\Documents\Algoritmos Jorge\Ejercicios\ejercicios_python\Python_Ej\ProyectoPython\Convertidordemoneda.py", line 13, in <module>
    #moneda=str(A.index(B))
#ValueError: substring not found

if moneda == "Dolar":
    print("Su moneda es: ", moneda)
    input("Que cantidad de dinero requieres convertir")
elif moneda == "Euro":
    print("Su moneda es: ", moneda)
    input("Digite la cantidad de dinero ")
else: 
    print("No existe esa moneda")






