Usuario = ("UsuarioEAN")
Contraseña = ("Uean2022")
user = False
contra = False

while user == False:
    inpUser = input("Ingresa tu usuario: ")
    if inpUser == Usuario:
        user = True
        print("Usuario correcto.")
    else:
        print("Usuario incorrecto, digitalo nuevamente")

while contra == False:
    if user == True:
        inpPass = input("Ingresa la contraseña: ")
        if inpPass == Contraseña:
            print("Contraseña correcta")
            contra = True
        else:
            print("Contraseña invalida, intentalo de nuevo")

    
    