print("Escriba dos numeros iguales: ")
condicion= 1
while condicion == 1:
    a, b = input("Inserte el primer número: "), input("Inserte el segundo número: ")
    if a != b:
        print("Es incorrecto, intentelo de nuevo.")
    else: 
        print("Es correcto!")    
        condicion = 2

