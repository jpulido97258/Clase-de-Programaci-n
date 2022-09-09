#break for

usuario = "mishi"
contraseña = "gatito123"

print("Ingrese su usuario:")
usuario1 = input()
print("Ingrese su contraseña")
contraseña1 = input()

if usuario1 == usuario and contraseña1 == contraseña:
    print("Bienvenido")
else:
    print("Usuario o contraseña incorrecto")