#Pedirle al usuario nombre, apelilldo, edad, responderle por consola si es mayor o menor de edad
Usuario = input("Por favor dime tu nombre y tu apellido: ")
Edad = int(input("Ingresa tu edad: "))

if Edad >= 18:
    print("Señor usuario", Usuario, "eres mayor de edad")
else:
    print("Señor usuario", Usuario, "eres menor de edad")