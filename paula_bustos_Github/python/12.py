#Poner contraseña, usario y contraseña correcta
var = input("Ingrese el usuario: ")
User = input("Ingrese la contraseña: ")
usuario = "ruiz"
contraseña = "profe"
for i in User:
    if User == contraseña and var == usuario:
        print("Bienvenido")
        break
    else:
        print("Lo sentimos el acceso sera denegado")
        break
