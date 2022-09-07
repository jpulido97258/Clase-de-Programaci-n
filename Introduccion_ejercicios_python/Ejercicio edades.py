#Este programa permite ingresar el nombre completo de una persona y la edad, ademas decir al final si la persona es mayor o menor de edad
print("A continuacion llena los datos solicitados")
#Se le solicitan datos al usuario
nombre = input("Ingresa el nombre o nombres de la persona: ")
apellidos = input("Ingresa los apellidos de la persona: ")
edad = input("Ingresa la edad: ")

#se definen los datos
nombre = str(nombre)
apellidos = str(apellidos)
edad = int(edad)

print("Segun al informacion digitada, el nombre completo de la persona es:" , nombre , apellidos, "y su edad es:" , edad)

#se hace el condicional de mayoria de edad
if edad>= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")