cont=1
while True:
    usuario =input("digite el usuario: ")
    tupla = tuple(usuario.split())

    contraseña = input("Digite su contrasña: ")
    tupla= tuple(contraseña.split())
    cont=cont+1
    if "UsuarioEAN" == usuario and "Uean2022" == contraseña:
        print ("Es correcto")
        break
    else:
        print ("Esta mal")