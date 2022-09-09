contraseña=[input('ingrese la contraseña')]
contador=0
while contador<4:
    contraseña=[input('ingrese la contraseña')]
    for n in contraseña:
        if n==('programación'):
            print('acceso concedido')
            break
        else:
            input('acceso denegado')
