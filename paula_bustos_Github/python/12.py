#Poner contraseña, usario y contraseña correcta
User = input("Ingrese la contraseña: ")
contraseña = "profe"
while True:
    for i in User:
        if User == contraseña:
            print("Esta bien")
            break
        elif User != contraseña:
            print("dwad")
            break
        else:
            User = input("Ingrese la contraseña: ")