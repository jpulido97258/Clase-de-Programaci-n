#Usuario y Contraseña


Usuario=str(input("Ingrese su usuario:"))
Contraseña=str(input("Ingrese su contraseña:"))

U="Sergio_15"
C="Tonalhydr4"

for n in Usuario:
    if Usuario == U:
        print("Su usuario es correcto")
        break
else:print("Su usuario es incorrecto")

for n in Contraseña:
    if Contraseña == C:
        print("Su contraseña es correcta")
        break
else:print("Su contraseña es incorrecta")