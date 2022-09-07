usuario, contraseña = "jp", "millos12"
contador = 0
while contador <= 3:
    user, passw = str(input("Introduzca el usuario :")), str(input("Introduza su contrasena: "))
    if user == usuario and passw == contraseña:
        print("Datos correctos")
        contador = 4
    else:
        print("Datos incorrectos, intente de nuevo.") 
        contador += 1
        if contador == 3:
            print("Ya no le quedan mas intentos")
            exit()



